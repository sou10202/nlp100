from gensim.models import KeyedVectors

word_vectors = KeyedVectors.load("src/word_vectors.kv")

with open('src/questions-words.txt', 'r') as file1, open('src/questions-words-output.txt', 'w') as file2:
    for line in file1:
        if line.startswith(':'):
            print(line, file=file2, end='')
            continue
        words = line.rstrip().split()
        similar_word = word_vectors.most_similar(positive=[words[1], words[2]], negative=[words[0]], topn=1)[0]
        print(line.rstrip(), similar_word[0], similar_word[1], sep='  ', file=file2)