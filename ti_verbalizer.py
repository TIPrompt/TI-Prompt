
class cybertweet_verbalizer():
    cybertweet_binary_topic_single_word = {
        "security_relevant": ["security"],
        "security_irrelevant": ["general"]
    }

    cybertweet_binary_topic_w2v_t50 = {
        "security_relevant": ["security", "bootpturbo", "solutions", "cybersecurity", "systems", "infrastructure",
                              "blockchain", "mobile", "consulting", "eset", "tech", "asap", "ryan", "carnot",
                              "stinsonleonard", "firewall", "news", "russia", "preventive", "integrating", "privacy",
                              "testing", "wide", "pkg", "chipset", "expo", "sonar", "crucial", "hacklab", "kalember",
                              "pass", "azure", "equifax", "travel", "fixes", "comprehensive", "pensar", "apply", "backup",
                              "facebook", "gdpr", "pentesting", "mustread", "strategy", "dadimagazinech", "response",
                              "proofpoint", "mitigation", "herndon", "custom", "discover"],
        "security_irrelevant": ["general", "slay", "torinickswho", "fortunately", "skeds", "tummy", "barrels", "cuaron", "lay", "ot",
                                "crises", "ucl", "minning", "rainfall", "fantastic", "exhibited", "acknowle", "editorial",
                                "casablanca", "commutes", "fewer", "smfh", "taper", "nec", "stepped", "pd", "streets",
                                "dives", "replaced", "globalwidemedia", "strippin", "transitioning", "thechriswatson",
                                "threads", "realizing", "depicts", "josephfcox", "hou", "unpacker", "concatenate",
                                "bangkokkeizai", "amattwilliams", "confirmation", "jen", "professionalism", "hooper",
                                "solidweb", "consequent", "perhaps", "ohio", "austinmcbroom"]

    }

    cybertweet_binary_relevance_single_word = {
        "security_relevant": ["relevant"],
        "security_irrelevant": ["irrelevant"]
    }

    cybertweet_binary_relevance_w2v_t50 = {
      "security_relevant": ['relevant', 'adaption', 'guidelines', 'cari', 'manner', 'razanturki', 'knittingquark', 'ararora', 'cutty', 'arsh', 'blossom', 'diagram', 'tons', 'lhn', 'trojantrek', 'peterdazeley', 'groundwater', 'nsagov', 'digitalcameraw', 'painandcats', 'affords', 'westgirlist', 'tess', 'michigan', 'thenun', 'bought', 'ideals', 'fie', 'wome', 'duba', 'cyberbreach', 'resilient', 'chsatl', 'wat', 'swamplands', 'scoping', 'princes', 'simulation', 'unpackd', 'hughes', 'shelter', 'canari', 'boxerlessbossk', 'foster', 'lborodesign', 'utepils', 'cultural', 'stevenj', 'muscat', 'polite', 'thet'],
      "security_irrelevant": ['irrelevant', 'hon', 'withaphdigital', 'correct', 'bama', 'awakening', 'favorites', 'realized', 'dives', 'naidoonet', 'feminine', 'funder', 'implemented', 'tongue', 'caroljallen', 'nec', 'assisted', 'songs', 'crush', 'understandable', 'fav', 'editorial', 'godlikemisha', 'julie', 'messaged', 'kirumi', 'littl', 'inclined', 'persist', 'mf', 'skeds', 'watched', 'adored', 'blogdelciso', 'pushed', 'worthwhile', 'astargazingfool', 'humanrights', 'aww', 'reeks', 'stoic', 'occurs', 'kafeeeeeeeeow', 'fangirl', 'bowling', 'swinging', 'homework', 'albums', 'workaround', 'malcom', 'minning']

    }
    
    cybertweet_multi_topic_single_word = {
        "ransomware": ["ransomware"],
        "ddos": ["ddos"],
        "leak": ["leak"],
        "general": ["general"],
        "vulnerability": ["vulnerability"],
        "botnet": ["botnet"]
    }
    cybertweet_multi_topic_w2v_t50 = {
        "ransomware": ['virus', 'hackers', 'cyberattack', 'driven', 'million', 'healthcare', 'compromised', 'join', 'ways', 'prevents', 'tip', 'victims', 'tips', 'cyberattacks', 'files', 'phishing', 'traffic', 'samsam', 'eoeo', 'ransomwar', 'ransom', 'sentinel', 'body', 'cryptycat', 'laws', 'cost', 'impede', 'rising', 'mechanism', 'victim', 'far', 'turning', 'forwarded', 'journalism', 'infographics', 'reports', 'inside', 'emails', 'barack', 'distributing', 'pga', 'mails', 'technology', 'detects', 'business', 'defense', 'notorious', 'pinch', 'computer', 'ransomware'],
        "ddos": ['get', 'servers', 'just', 'poker', 'party', 'tk', 'overall', 'guard', 'making', 'glitch', 'discrimination', 'webinar', 'heavy', 'gameplay', 'offline', 'recorded', 'getting', 'uk', 'dissed', 'meshing', 'colder', 'slobbering', 'ranged', 'provider', 'hit', 'mgk', 'game', 'bank', 'disconnected', 'byronacohido', 'blocked', 'cryptowhispers', 'macers', 'investigated', 'coming', 'today', 'airlines', 'calling', 'stop', 'bbotezatu', 'ranked', 'sauce', 'xbox', 'call', 'effor', 'dick', 'website', 'ubisoft', 'disinformation', 'ddos'],
        "leak": ['sensitive', 'customer', 'breach', 'credit', 'brea', 'mspy', 'mgmtvisit', 'leaked', 'airways', 'accidentally', 'cen', 'cdrom', 'exo', 'equifax', 'tomcnamara', 'exfiltration', 'institutions', 'joeygee', 'mastercard', 'implicitbias', 'card', 'dutch', 'pipeline', 'breadth', 'field', 'bop', 'personal', 'objects', 'ntfs', 'cards', 'br', 'collecting', 'exif', 'uninitialized', 'thef', 'risking', 'pan', 'submitted', 'memory', 'deletes', 'bcz', 'ntt', 'montr', 'disi', 'ey', 'reporte', 'whitesourcesoft', 'transact', 'miami', 'data', 'leak'],
        "general": ['slay', 'torinickswho', 'fortunately', 'skeds', 'tummy', 'barrels', 'cuaron', 'lay', 'ot', 'crises', 'ucl', 'minning', 'rainfall', 'fantastic', 'exhibited', 'acknowle', 'editorial', 'casablanca', 'commutes', 'fewer', 'smfh', 'taper', 'nec', 'stepped', 'pd', 'streets', 'dives', 'replaced', 'globalwidemedia', 'strippin', 'transitioning', 'thechriswatson', 'threads', 'realizing', 'depicts', 'josephfcox', 'hou', 'unpacker', 'concatenate', 'bangkokkeizai', 'amattwilliams', 'confirmation', 'jen', 'professionalism', 'hooper', 'solidweb', 'consequent', 'perhaps', 'ohio', 'austinmcbroom', 'general'],
        "vulnerability": ['strength', 'physical', 'vulnerabili', 'vulner', 'vulnerabi', 'vulnerabilit', 'presence', 'confid', 'engagement', 'change', 'courage', 'act', 'sadc', 'flaws', 'honesty', 'intimacy', 'greatest', 'althenative', 'radically', 'vapt', 'struggles', 'emotion', 'beliefs', 'life', 'role', 'equates', 'passion', 'line', 'requires', 'authenticity', 'heart', 'relationship', 'emotions', 'vulnerabilities', 'bows', 'music', 'empathy', 'preparedness', 'collaborative', 'mailbox', 'cu', 'creativity', 'trusts', 'maturity', 'heartbreaking', 'flaw', 'normalizing', 'ignorance', 'context', 'broken', 'vulnerability'],
        "botnet": ['jdelacruz', 'botnets', 'iotsecurity', 'mirai', 'xmrig', 'botn', 'gafgyt', 'owari', 'healthcareit', 'smartcities', 'lesser', 'invention', 'nazis', 'cmdphp', 'iot', 'mud', 'targetting', 'indicted', 'zombies', 'aim', 'iatrogenesis', 'usa', 'canada', 'bti', 'hakai', 'wearables', 'extracting', 'link', 'cwbriefing', 'bot', 'satori', 'italy', 'spews', 'enormous', 'scope', 'commanded', 'anthem', 'usnistgov', 'offices', 'fakhuushashim', 'computers', 'media', 'evil', 'fisher', 'collection', 'sensors', 'retardation', 'lachie', 'darkhydrus', 'backtoschool', 'botnet']

    }

class vultweet_verbalizer():
    vultweet_template_topic_singe_word = {
        "vulnerability_relevant": ["vulnerability"],
        "vulnerability_irrelevant": ["general"]
    }

    vultweet_template_topic_w2v_t50 = {
        "vulnerability_relevant": ['vulnerability', 'flaw', 'vulnerabilities', 'threatmeter', 'vuln', 'cve', 'na', 'exploit', 'topic',
                                   'engine', 'bugtraq', 'bug', 'unspecified', 'exploitdb', 'jung', 'universal',
                                   'appliance', 'patient', 'cs', 'suite', 'remote', 'disclosure', 'arbitrary', 'befo',
                                   'middleware', 'opentext', 'insecure', 'cryptography', 'packetstorm', 'manager',
                                   'implementation', 'gerrit', 'drupal', 'abap', 'flaws', 'openssl', 'cxsecurity',
                                   'pdfium', 'xml', 'outside', 'validation', 'antenna', 'syss', 'fusion', 'webcenter',
                                   'bigfix', 'configuration', 'function', 'regression', 'xss', 'row'],
        "vulnerability_irrelevant": ['general', 'geoffbelknap', 'monishb', 'cluster', 'coloring', 'setbacks', 'babes',
                                     'vodafoneuk', 'sans_edu', 'jennifer_arcuri', 'reg', 'strasner', 'colts', 'craft',
                                     'adult', 'washington', 'coach', 'fg', 'bec', 'mindsets', 'sans_isc', 'buccaneers',
                                     'wearables', 'ls', 'plusvic', 'ullrich', 'subcomponent', 'butler', 'mechanims',
                                     'hourglass', 'slayer', 'feminism', 'coo', 'judithsimoracle', 'strategic',
                                     'kasireddy', 'centers', 'protecttoenable', 'dvms', 'ele', 'dungy', 'ndbapi',
                                     'att', 'bitbucket', 'sport', 'cathywalker', 'islamic', 'cardinal', 'kasim',
                                     'strategically', 'president']
    }

    vultweet_binary_relevance_single_word = {
        "vulnerability_relevant": ["relevant"],
        "vulnerability_irrelevant": ["irrelevant"]
    }
    vultweet_binary_relevance_w2v_top50 = {
        "vulnerability_relevant": ['preventio', 'stays', 'authentic', 'cloudlens', 'idg', 'apac', 'slap', 'avg', 'fac', 'ids', 'contributor', 'glob', 'machetes', 'aircrack', 'aibireland', 'elk', 'hertz', 'coupled', 'tsq', 'infosys', 'securitytube', 'swords', 'gcs', 'evolve', 'profits', 'shifts', 'imc', 'ixiacom', 'avaiki', 'caches', 'soo', 'versio', 'extrahop', 'protecttoenable', 'poisoned', 'derivative', 'massively', 'platfo', 'oracledatacloud', 'cottage', 'entire', 'pervasive', 'internships', 'monitoring', 'wceu', 'scholarships', 'bmeurer', 'enriched', 'jradcliffe', 'cdameffmd', 'relevant'],
        "vulnerability_irrelevant": ['arc', 'internacional', 'twtteer', 'tica', 'smosser', 'vader', 'katebevan', 'linuxmagic', 'aaronwoland', 'dakacki', 'chromiumdev', 'thevickingtor', 'samurai', 'morisson', 'linguistics', 'cybersecrobert', 'stevelord', 'grc', 'brownteaming', 'smuggled', 'malwareunicorn', 'surfer', 'paging', 'twiteer', 'bista', 'joernchen', 'cyberneticist', 'twitteer', 'perplexed', 'thx', 'lenin', 'gigastacey', 'nos', 'ethanol', 'warrior', 'wikipedia', 'dotslashpipe', 'amtwo', 'cola', 'anonyspain', 'dsl', 'quoteform', 'kristofera', 'arthur', 'peabnuts', 'kpoulsen', 'erik', 'yeay', 'theoracleytu', 'macworlduk', 'irrelevant']
    }
