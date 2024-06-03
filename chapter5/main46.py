from main41 import div_chunks

def verb_particle_nouns(sentences):
    result = []
    for sentence in sentences:
        for chunk in sentence:
            for morphs in chunk.morphs:
                if morphs.pos == '動詞':
                    if len(chunk.srcs):
                        word_by = ''
                        noun_by = []
                        word_dic = {}
                        for src in chunk.srcs:
                            for x in sentence[src].morphs:
                                if x.pos != '記号':
                                    word_by += x.surface
                                if x.pos == '助詞':
                                    noun_by.append(x.surface)
                                    word_dic[x.surface] = word_by
                                    word_by = ''
                            word_by = ''
                        if len(noun_by):
                            noun_by = sorted(list(set(noun_by)))
                            result.append(morphs.base + '\t' + ' '.join(noun_by)+ '\t '+ ' '.join([word_dic[x] for x in noun_by]))
    with open('out/result46.txt', 'w') as f:
        for line in result:
            print(line, file=f)

def main():
    sentences = div_chunks()
    verb_particle_nouns(sentences)

if __name__ == '__main__':
    main()