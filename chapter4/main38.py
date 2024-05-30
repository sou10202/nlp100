from main30 import load_mecab
import itertools, collections, csv, pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

path = 'src/neko.txt'
mecab_list = load_mecab(path)

result = []
for line in mecab_list:
    for word in line:
            if word['pos'] != '補助記号' :
                result.append(word['surface'])

cnt_words = collections.Counter(result)
plt.hist(cnt_words.values(), range(1, 100))

plt.savefig('out/neko_mode.png')
plt.close('all')