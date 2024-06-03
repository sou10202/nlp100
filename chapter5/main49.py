from itertools import combinations
from main41 import div_chunks

def get_path_to_root(now, sentence):
    chunk = sentence[now]
    path = []
    if chunk.dst != -1:
        path.append(now)
        nxt = chunk.dst
        while nxt != -1:
            path.append(nxt)
            nxt = sentence[nxt].dst
    return path

def extract_nouns(sentence):
    nouns = []
    for i, chunk in enumerate(sentence):
        if '名詞' in [morph.pos for morph in chunk.morphs]:
            nouns.append(i)
    return nouns

def make_pair_nouns(sentence, nouns):
    for i, j in combinations(nouns, 2):
        pathx = get_path_to_root(i, sentence)
        pathy = get_path_to_root(j, sentence)
        path1 = []
        path2 = []
        path3 = []
        flag = False
        if j in pathx:
            for k in pathx:
                if k == i:
                    morphs = 'X' + ''.join([x.surface if x.pos == '助詞' else '' for x in sentence[k].morphs])
                    path1.append(''.join(morphs))
                elif k != j:
                    morphs = ''.join([x.surface if x.pos != '記号' else '' for x in sentence[k].morphs])
                    path1.append(''.join(morphs))
                else:
                    morphs = 'Y' + ''.join([x.surface if x.pos == '助詞' else '' for x in sentence[k].morphs])
                    path1.append(''.join(morphs))
                    break
                print(' -> '.join(path1))
        else:
            for k in pathx:
                if k == i:
                    morphs = 'X' + ''.join([x.surface if x.pos == '助詞' else '' for x in sentence[k].morphs])
                    path1.append(''.join(morphs))
                elif k not in pathy:
                    morphs = ''.join([x.surface if x.pos != '記号' else '' for x in sentence[k].morphs])
                    path1.append(''.join(morphs))
                else:
                    break
            for l in pathy:
                if l == j:
                    morphs = 'Y' + ''.join([x.surface if x.pos == '助詞' else '' for x in sentence[l].morphs])
                    path2.append(''.join(morphs))
                elif l != k:
                    morphs = ''.join([x.surface if x.pos != '記号' else '' for x in sentence[k].morphs])
                    path2.append(''.join(morphs))
                elif l == k or flag:
                    flag = True
                    morphs = ''.join([x.surface if x.pos != '記号' else '' for x in sentence[l].morphs])
                    path3.append(''.join(morphs))
            print(' -> '.join(path1) + ' | ' + ' -> '.join(path2) + ' | ' + ' -> '.join(path3))

def main():
    sentences = div_chunks()
    nouns = extract_nouns(sentences[2])
    make_pair_nouns(sentences[2], nouns)

if __name__ == '__main__':
    main()