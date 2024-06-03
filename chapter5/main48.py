from main41 import div_chunks

def get_path(sentences):
    for sentence in sentences:
        for chunk in sentence:
            pos_list = [x.pos for x in chunk.morphs]
            if '名詞' in pos_list and chunk.dst != -1:
                path = [''.join(x.surface if x.pos != '記号' else '' for x in chunk.morphs)]
                next_dst = chunk.dst
                while next_dst != -1:
                    path.append(''.join([x.surface if x.pos != '記号' else '' for x in sentence[next_dst].morphs]))
                    next_dst = sentence[next_dst].dst
                print('->'.join(path))

def main():
    sentences = div_chunks()
    get_path(sentences[:3])

if __name__ == '__main__':
    main()