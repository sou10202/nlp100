from main41 import div_chunks

def verb_particle(sentences):
    result = []
    for sentence in sentences:
        for chunk in sentence:
            for morphs in chunk.morphs:
                if morphs.pos == '動詞':
                    if len(chunk.srcs):
                        word_by = []
                        for src in chunk.srcs:
                            word_by += [x.base for x in sentence[src].morphs if x.pos == '助詞']
                        if len(word_by):
                            word_by = sorted(list(set(word_by)))
                            result.append(morphs.base + '\t' + ' '.join(word_by))
    with open('out/result45.txt', 'w') as f:
        for line in result:
            print(line, file=f)

def main():
    sentences = div_chunks()
    verb_particle(sentences)

if __name__ == '__main__':
    main()
