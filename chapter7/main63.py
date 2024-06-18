from gensim.models import KeyedVectors

word_vectors = KeyedVectors.load("src/word_vectors.kv")

spain = word_vectors["Spain"]
madrid = word_vectors["Madrid"]
athens = word_vectors["Athens"]

result_vector = spain - madrid + athens
result_vector2 = spain + athens - madrid
print('===類似単語===')
# print(word_vectors.most_similar(result_vector2))
print(word_vectors.most_similar(positive=['Spain', 'Athens'], negative=['Madrid']))