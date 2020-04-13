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
surfaces = collections.Counter(surface).most_common(10)

surfaces_x = [x[1] for x in surfaces]
surfaces_y = [x[0] for x in surfaces]

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'AppleMyungjo'
a = np.array([1,2,3,4,5,6,7,8,9,10])
plt.bar(a,surfaces_x,color='#7D6BA0',align='center',edgecolor='white')
plt.title('頻度上位10語')

plt.xticks(a,surfaces_y)

plt.show()



