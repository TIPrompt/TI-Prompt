import argparse


def get_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default=None, type=str, required=True,
                        help="The input data dir, containing the train and eval data json files.", )
    parser.add_argument("--model_type", default='bert', type=str, required=True,
                        help="The language model type")
    parser.add_argument("--model_name", default='bert-base-cased', type=str, required=True,
                        help="Specific the model name")
    parser.add_argument("--device_num", default=0, type=int, required=True,
                        help="Specific cuda device number")
    return parser