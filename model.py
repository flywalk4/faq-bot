"""
pip install -q deeppavlov
python3 -m deeppavlov install fasttext_logreg 
python3 -m deeppavlov interact fasttext_logreg -d  
pip install fasttext-wheel
"""
from deeppavlov import build_model
from deeppavlov.core.common.file import read_json, find_config
from deeppavlov import train_model
from pathlib import Path

from deeppavlov.core.data.utils import download
x = find_config('fasttext_logreg')
print(x)    
model_config = read_json(x)
model_config['metadata']['variables']['LANGUAGE'] = 'ru'
model_config['metadata']['variables']['SPACY_MODEL'] = 'ru_core_news_sm'
#model_config['metadata']['download'] = "https://storage.yandexcloud.net/faq/ru.bin"
#model_config['dataset_reader']['data_path'] = "train.json"
#model_config['dataset_reader']['url'] = "https://storage.yandexcloud.net/faq/train2.csv"
model_config['dataset_reader']['format'] = "csv"
model_config['dataset_reader']['x'] = "Question"
model_config['dataset_reader']['y'] = "Answer"
model_config['dataset_reader']['sep'] = ","

faq = train_model(model_config)
print(faq)
