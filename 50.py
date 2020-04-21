import re


def line_get():
    s = []
    ss = []
    with open('./nlp.txt','r') as f:
        comp = re.compile(r'''(?<=[.;:?!])\s(?=[A-Z])''')
        for line in f:
            line = line.strip('\n')
            if len(line) != 0:
                s = re.split(comp, line)
                for i in range(0, len(s)):
                    print(s[i])

line_get()

