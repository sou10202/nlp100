from main30 import load_mecab
import itertools, collections, csv, pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

path = 'src/neko.txt'
mecab_list = load_mecab(path)

result = []
for line in mecab_list:
    for word in line:
        result.append(word['surface'])

c = collections.Counter(result)
rank = sorted(c.values(), reverse=True)
print(rank)
plt.plot(rank)
plt.xscale('log')
plt.yscale('log')
plt.savefig('out/word_zipf.png')
plt.close('all')