from main30 import load_mecab
import itertools, collections, csv, pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

path = 'src/neko.txt'
mecab_list = load_mecab(path)

result = []
for line in mecab_list:
    if any (word['surface'] == '猫' for word in line):
        wordinline = []
        for word in line:
            if word['pos'] != '補助記号' and word['pos'] != '空白' and word['surface'] != '猫':
                result.append(word['surface'])

cnt_words = collections.Counter(result).most_common()

x_word = []
y_count = []
for word, count in cnt_words:
    x_word.append(word)
    y_count.append(count)

plt.bar(x=x_word[:10], height=y_count[:10])

plt.savefig('out/neko_coword.png')
plt.close('all')