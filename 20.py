import json
def read_wiki(fname,title):
    with open(fname,'rt') as date_file:
        for line in date_file:
            date_json=json.loads(line)
            if date_json['title']==title:
                return date_json['text']
def main():
    fname = 'jawiki-country.json.gz'
    print(read_wiki(fname, 'イギリス'))
if __name__=='__main__':
    main()