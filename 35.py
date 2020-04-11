import MeCab
import more_itertools as mit

mecab = MeCab.Tagger()

with open('./neko.txt') as in_file, open('./neko.txt.mecab', mode='w') as out_file:
    out_file.write(mecab.parse(in_file.read()))

with open("neko.txt.mecab") as f:
    nums = []
    surface = []
    for i, line in enumerate(f):
        split_line = line.rstrip("\r\n").split("\t")
        if len(split_line) > 1:
            morpheme_map = split_line[1].split(",")
            surface.append(split_line[0])
            if morpheme_map[0] == "名詞":
                nums.append(i)

nums_sp =[list(group) for group in mit.consecutive_groups(nums)]

noun = []
nouns = []
for i in range(len(nums_sp)):
    if len(nums_sp[i]) > 1:
        for a in nums_sp[i]:
            noun.append(surface[a])
        noun= [''.join(noun)]
        nouns.append(noun)
        noun = []
print(nouns)






