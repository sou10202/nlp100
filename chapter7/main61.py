from gensim.models import KeyedVectors

word_vectors = KeyedVectors.load("src/word_vectors.kv")

print(word_vectors.similarity("United_States", "U.S."))