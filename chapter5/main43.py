from main41 import div_chunks

def extract_n_v(sentence):
    for chunk in sentence:
        if chunk.dst != -1:
            word_to = [x.pos for x in chunk.morphs]
            word_by = [x.pos for x in sentence[chunk.dst].morphs]
            if ('名詞' in word_to) and ('動詞' in word_by):
                nouns = ''.join([x.surface if x.pos != '記号' else '' for x in chunk.morphs])
                verbs = ''.join([x.surface if x.pos != '記号' else '' for x in sentence[chunk.dst].morphs])
                print(nouns, verbs, sep='\t')

def main():
    sentences = div_chunks()
    extract_n_v(sentences[1])

if __name__ == '__main__':
    main()