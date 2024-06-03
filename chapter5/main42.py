from main41 import Chunk, div_chunks
from main40 import Morph

def extract_word(sentence):
    for chunk in sentence:
        if chunk.dst != -1:
            word_to = ''.join([x.surface if x.pos != '記号' else '' for x in chunk.morphs])
            word_by = ''.join([x.surface if x.pos != '記号' else '' for x in sentence[chunk.dst].morphs])
        print(word_to, word_by, sep='\t')

def main():
    sentences = div_chunks()
    extract_word(sentences[1])

if __name__ == '__main__':
    main()