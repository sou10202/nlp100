import re
class Morph:
    def __init__(self, line):
        surface = line.split('\t')
        others = surface[1].split(',')
        self.surface = surface[0]
        self.base = others[6]
        self.pos = others[0]
        self.pos1 = others[1]

    def __str__(self):
        return 'surface: {}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)
    
    def __repr__(self):
        return self.surface

def read_parsed_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    morphs = []
    for line in lines:
        if bool(re.search(r'^\*', line)):
            continue
        if line == 'EOS\n':
            continue
        morphs.append(Morph(line))
    return morphs

def main():
    morphs = read_parsed_file('src/ai.ja.txt.parsed')
    for morph in morphs[:10]:
        print(morph)

if __name__ == '__main__':
    main()
