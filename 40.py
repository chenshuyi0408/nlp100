class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


with open(r'neko.txt.cabocha', mode="r") as f:
    morphemes = []
    morphemes_list = []
    for line in f:
        split_line = line.rstrip("\n").split("\t")
        if len(split_line) > 1:
            morpheme_map = split_line[1].split(",")
            morphemes.append(Morph(split_line[0], morpheme_map[6], morpheme_map[0], morpheme_map[1]))
        elif split_line[0] == "EOS":
            morphemes_list.append(morphemes)
            morphemes = []

for item in morphemes_list[2]:
    print('surface={}\tbase={}\tpos={}\tpos1={}'.format(item.surface, item.base, item.pos, item.pos1))