from gensim.models import KeyedVectors

# Path to the word vector file
word_vector_file = "src/GoogleNews-vectors-negative300.bin.gz"

word_vectors = KeyedVectors.load_word2vec_format(word_vector_file, binary=True)

# Access word vectors
vector = word_vectors["United_States"]
print(vector)

word_vectors.save("src/word_vectors.kv")
### use scipy version 1.11.4 ###