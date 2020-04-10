import MeCab
mecab = MeCab.Tagger()

with open('./neko.txt') as in_file, open('./neko.txt.mecab', mode='w') as out_file:
    out_file.write(mecab.parse(in_file.read()))

with open("neko.txt.mecab") as f:
    surface = []
    pos = []
    for i, line in enumerate(f):
        split_line = line.rstrip("\r\n").split("\t")
        if len(split_line) > 1:
            morpheme_map = split_line[1].split(",")
            surface.append(split_line[0])
            pos.append(morpheme_map[0])

for i in range(len(surface)-2):
    if pos[i+2] == "名詞" and pos[i] == "名詞" and surface[i+1] == "の":
        print(surface[i],surface[i+1],surface[i+2])
