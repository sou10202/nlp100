from gensim.models import KeyedVectors

word_vectors = KeyedVectors.load("src/word_vectors.kv")

print('===単語  類似度===')
for word in word_vectors.most_similar('United_States'):
    print(word[0], word[1], sep='  ')