import MeCab

def morphpology(file_path):
    mecab = MeCab.Tagger()
    with open(file_path, 'r') as f, open(file_path + '.mecab', 'w') as f2:
        lines = f.readlines()
        for text in lines:
            result = mecab.parse(text)
            print(result, file=f2)

def load_mecab(file_path):
    with open(file_path + ".mecab", 'r') as f:
        lines = f.readlines()
        ans_all = []
        ans_line = []
        for line in lines:
            if (line == 'EOS\n') or (line == '\n'):
                continue
            result = {}
            line = line.split('\t')
            result['surface'] = line[0]
            result['base'] = line[3]
            pos = line[4].split('-')
            result['pos'] = pos[0]
            if (len(pos) != 1):
                result['pos1'] = pos[1]
            else:
                result['pos1'] = ''
            ans_line.append(result)
            if line[0] == "。":
                ans_all.append(ans_line)
                ans_line = []
    return (ans_all)

def main():
    file_path = 'src/neko.txt'
    morphpology(file_path=file_path)
    result = load_mecab(file_path)

if __name__ == '__main__':
    main()