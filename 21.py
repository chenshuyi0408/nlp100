import json
import re

def read_wiki(fname,title):
    with open(fname,'rt') as data_file:
        for line in data_file:
            data_json=json.loads(line)
            if data_json['title']==title:
                return data_json['text']
def is_category(string):
    return re.match(r'^\[\[Category:.+\]\]$', string)
def main():
    fname='jawiki-country.json.gz'
    text=read_wiki(fname,'イギリス').split('\n')
    for line in text:
        if is_category(line):
            print(line)
main()