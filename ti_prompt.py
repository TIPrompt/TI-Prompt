from sklearn import metrics
import torch
from openprompt import PromptForClassification
from openprompt.prompts import ManualTemplate, ManualVerbalizer
from torch.optim import AdamW

from ti_templates import SingleTemplate
from ti_verbalizer import cybertweet_verbalizer, vultweet_verbalizer
from run_argparse import get_argparse
from util import file_util
from openprompt.data_utils import InputExample, InputFeatures
from openprompt.plms import load_plm
from torch.utils.data import DataLoader, RandomSampler

def data_load(data_path):
    dataset = {}
    dataset['train'] = []
    # the data file names need to be consistent with the real file name
    train_data = file_util.jsonfile_to_dict(data_path + "train_data.json")
    eval_data = file_util.jsonfile_to_dict(data_path + "eval_data.json")
    for index, data in enumerate(train_data):
        input_example = InputExample(text_a=data[0], label=int(data[1]), guid=index)
        dataset['train'].append(input_example)
    print("Train Data Example: ", dataset['train'][0])

    dataset['valid'] = []
    for index, data in enumerate(eval_data):
        input_example = InputExample(text_a=data[0], label=int(data[1]), guid=index)
        dataset['valid'].append(input_example)
    print("Train Data Example: ", dataset['valid'][0])
    return dataset

def get_template(template_text_list, tokenizer):
    template_list = []
    for template in template_text_list:
        temp_template = ManualTemplate(tokenizer=tokenizer, text=template)
        template_list.append(temp_template)
    return template_list


def get_verbalizer(verbalizer_dict, tokenizer):
    label_words = []
    class_num = len(verbalizer_dict.keys())
    for class_ in verbalizer_dict.keys():
        label_words.append(verbalizer_dict[class_])

    verbalizer = ManualVerbalizer(tokenizer, num_classes=class_num,
                                    label_words=label_words)
    print(verbalizer.label_words_ids)
    logits = torch.randn(class_num, len(tokenizer))
    verbalizer.process_logits(logits)
    return verbalizer

def prompt_prepare(model_type, model_name, ):
    plm, tokenizer, model_config, WrapperClass = load_plm(model_type, model_name)
    return plm, tokenizer, model_config, WrapperClass

def data_wrap(template_list, wrapclass, tokenizer, datasets):
    wrapped_t5tokenizer = wrapclass(max_seq_length=128, decoder_max_length=3, tokenizer=tokenizer,
                                       truncate_method="head")
    model_inputs = {
        "train": [],
        "valid": []
    }
    # train wrap
    for sample in datasets["train"]:
        for template in template_list:
            temp_input_features = InputFeatures(
                **wrapped_t5tokenizer.tokenize_one_example(template.wrap_one_example(sample), teacher_forcing=False),
                **template.wrap_one_example(sample)[1]).to_tensor()
            model_inputs["train"].append(temp_input_features)
    for sample in datasets["valid"]:
        for template in template_list:
            temp_input_features = InputFeatures(
                **wrapped_t5tokenizer.tokenize_one_example(template.wrap_one_example(sample), teacher_forcing=False),
                **template.wrap_one_example(sample)[1]).to_tensor()
            model_inputs["valid"].append(temp_input_features)
    return model_inputs


def train(plm, template, verbalizer, train_dataloader, eval_dataloader, device_num):
    use_cuda = True
    prompt_model = PromptForClassification(plm=plm, template=template, verbalizer=verbalizer, freeze_plm=False)
    if use_cuda:
        prompt_model = prompt_model.cuda(device_num)
    loss_func = torch.nn.CrossEntropyLoss()
    no_decay = ['bias', 'LayerNorm.weight']
    optimizer_grouped_parameters = [
        {'params': [p for n, p in prompt_model.named_parameters() if not any(nd in n for nd in no_decay)],
         'weight_decay': 0.01},
        {'params': [p for n, p in prompt_model.named_parameters() if any(nd in n for nd in no_decay)],
         'weight_decay': 0.0}
    ]

    optimizer = AdamW(optimizer_grouped_parameters, lr=1e-4)
    epoches = 10
    device_str = "cuda:" + str(device_num)
    for epoch in range(epoches):
        tot_loss = 0
        for step, inputs in enumerate(train_dataloader):
            if use_cuda:
                inputs = inputs.to(device_str)
            logits = prompt_model(inputs)
            labels = inputs['label']
            loss = loss_func(logits, labels)
            loss.backward()
            tot_loss += loss.item()
            optimizer.step()
            optimizer.zero_grad()
            if step % 100 == 0:
                print("Epoch {}, step {},  average loss: {}".format(epoch, step, tot_loss / (step + 1)), flush=True)
    eval(eval_dataloader, use_cuda, prompt_model, device_num)

def eval(eval_dataloader, use_cuda, prompt_model, device_num):
    print("Eval\n")
    allpreds = []
    alllabels = []
    device_str = "cuda:" + str(device_num)
    for step, inputs in enumerate(eval_dataloader):
        if use_cuda:
            inputs = inputs.to(device_str)
        logits = prompt_model(inputs)
        labels = inputs['label']
        alllabels.extend(labels.cpu().tolist())
        allpreds.extend(torch.argmax(logits, dim=-1).cpu().tolist())

    evaluation_metrics(allpreds, alllabels)

def evaluation_metrics(pred, label):
    precision = 0 if len(label) == 0 else metrics.precision_score(label, pred, zero_division=0, average='weighted')
    recall = 0 if len(label) == 0 else metrics.recall_score(label, pred, zero_division=0, average='weighted')
    f1 = 0 if len(label) == 0 else metrics.f1_score(label, pred, zero_division=0, average='weighted')
    acc = 0 if len(label) == 0 else metrics.accuracy_score(label, pred)
    print("Sklearn metrics: P: {}, R: {}, F1: {}, Acc:{}".format(precision, recall, f1, acc))

if __name__ == '__main__':
    args = get_argparse().parse_args()
    print(args)
    datasets = data_load(data_path=args.data_path)
    plm, tokenizer, model_config, WrapperClass = prompt_prepare(model_type=args.model_type, model_name=args.model_name)

    # select a template from the templates.py
    template_text_list = SingleTemplate.single_vulnerability_relevance_template
    print("Template:", template_text_list)
    templates = get_template(template_text_list, tokenizer=tokenizer)
    model_input = data_wrap(template_list=templates, wrapclass=WrapperClass, tokenizer=tokenizer, datasets=datasets)

    # select a verbalizer from the verbalizer.py, which should be consistent with the template
    verbalizer_dict = vultweet_verbalizer.vultweet_binary_relevance_w2v_top50
    print("Verbalizer:", verbalizer_dict)
    verbalizer = get_verbalizer(verbalizer_dict, tokenizer)
    train_sampler = RandomSampler(model_input["train"])
    train_dataloader = DataLoader(model_input["train"], sampler=train_sampler, batch_size=4,
                                  collate_fn=InputFeatures.collate_fct)
    eval_sampler = RandomSampler(model_input["valid"])
    eval_dataloader = DataLoader(model_input["valid"], sampler=eval_sampler, batch_size=4,
                                 collate_fn=InputFeatures.collate_fct)

    # train
    train(plm, templates[0], verbalizer, train_dataloader, eval_dataloader, args.device_num)
