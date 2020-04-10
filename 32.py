import MeCab
mecab = MeCab.Tagger()

with open('./neko.txt') as in_file, open('./neko.txt.mecab', mode='w') as out_file:
    out_file.write(mecab.parse(in_file.read()))

def get_neko_morphemes():
    with open("neko.txt.mecab") as f:
        genkei = []
        genkeis = []
        for i, line in enumerate(f):
            split_line = line.rstrip("\r\n").split("\t")
            if len(split_line) > 1:  #'EOS'
                morpheme_map = split_line[1].split(",")
                if morpheme_map[0] == "動詞":
                    genkei = morpheme_map[6]
                    genkeis.append(genkei)
    return genkeis

result = get_neko_morphemes()
print(result)