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

fre = collections.Counter(surfaces)
fres = []

for value in fre.values():
    fres.append(value)
fres = collections.Counter(fres)


f = zip(fres.values(),fres.keys())
f = sorted(f,reverse = True)

ka = [i[0] for i in f]
va = range(1,len(ka)+1)

import matplotlib.pyplot as plt
plt.loglog(va, ka)

plt.show()