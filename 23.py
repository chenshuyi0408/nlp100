
import json
import re


def read_wiki(fname, tiltle):
    with open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']


def is_section(string):
    return re.match(r'^=+.+=+$', string)


def get_section_level(string):
    m = re.match(r'^(=+)(.+?)=+$', string)
    return ' name : {0}\tlevel : {1} '.format(m.group(2), len(m.group(1)) - 1)


def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname, 'イギリス').split('\n')

    for line in text:
        if is_section(line):
            print(get_section_level(line))


if __name__ == '__main__':
    main()