from main41 import div_chunks

def verb_particle_nouns(sentences):
    result = []
    for sentence in sentences:
        for chunk in sentence:
            candidate = ''
            for morphs in chunk.morphs:
                if morphs.pos == '動詞':
                    if len(chunk.srcs):
                        word_by = ''
                        noun_by = []
                        word_dic = {}
                        flag2 = False
                        for src in chunk.srcs:
                            flag = False
                            for x in sentence[src].morphs:
                                if x.pos == '名詞' and x.pos1 == 'サ変接続' and not flag2:
                                    candidate += x.surface
                                    flag = True
                                    continue
                                elif x.pos == '助詞' and x.surface == 'を' and flag and not flag2:
                                    candidate += 'を'
                                    flag = False
                                    flag2 = True
                                    continue
                                if x.pos != '記号':
                                    flag = False
                                    word_by += x.surface
                                if x.pos == '助詞':
                                    flag = False
                                    noun_by.append(x.surface)
                                    word_dic[x.surface] = word_by
                                    word_by = ''
                                else:
                                    flag = False
                            word_by = ''
                        if len(noun_by) and flag2:
                            noun_by = sorted(list(set(noun_by)))
                            result.append(candidate + morphs.base + '\t' + ' '.join(noun_by)+ '\t '+ ' '.join([word_dic[x] for x in noun_by]))
    with open('out/result47.txt', 'w') as f:
        for line in result:
            print(line, file=f)

def main():
    sentences = div_chunks()
    verb_particle_nouns(sentences)

if __name__ == '__main__':
    main()