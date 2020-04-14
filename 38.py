import MeCab
import collections

mecab = MeCab.Tagger()

with open('./neko.txt') as in_file, open('./neko.txt.mecab', mode='w') as out_file:
    out_file.write(mecab.parse(in_file.read()))

with open("neko.txt.mecab") as f:
    surface = []
    for i, line in enumerate(f):
        split_line = line.rstrip("\r\n").split("\t")
        if len(split_line) > 1:
            surface.append(split_line[0])

surfaces = []
surfaces = collections.Counter(surface)

fre = []
for v in surfaces.values():
    fre.append(v)

import matplotlib.pyplot as plt
plt.hist(fre, bins=20, rwidth=0.8,range=(1, 20))


plt.xlabel('出現頻度',fontproperties='AppleMyungjo')
plt.ylabel('単語種類数',fontproperties='AppleMyungjo')

plt.show()


