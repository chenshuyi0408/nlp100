import re


def line_get():
    s = []
    fi = open('./nlp50.txt','w',encoding='utf-8')
    with open('./nlp.txt','r') as f:
        comp = re.compile(r'''(?<=[.;:?!])\s(?=[A-Z])''')
        for line in f:
            line = line.strip('\n')
            if len(line) != 0:
                s = re.split(comp, line)
                for i in range(0, len(s)):
                    fi.writelines(s[i]+'\n')
    f.close()
    with open('./nlp50.txt', 'r') as f:
        print(f.read())

line_get()

