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
            if word['pos'] != '補助記号' and word['pos'] != '空白':
                wordinline.append(word['surface'])
        result.append(wordinline)

pair_list = [list(itertools.combinations(n, 2)) for n in result if len(result) >= 2]

all_pairs = []
for u in pair_list:
    all_pairs.extend(u)

# # print(all_pairs)
# print([all_pairs[i] for i in range(20)])

pairs_sorted = []
for pair in all_pairs:
    pairs_sorted.append(tuple(sorted(pair)))
    

cnt_pairs = collections.Counter(pairs_sorted).most_common()
with open('out/pair_count.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pair', 'count'])
    writer.writerows(cnt_pairs)

cnt_words = []


df = pd.read_csv('out/pair_count.csv')
df_neko = df[df['pair'].str.contains("'猫'")]

label_x = [pair.replace("'猫'", "") for pair in df['pair']]
df_neko[:10].plot.bar(x = 'pair')

plt.savefig('out/neko_pair.png')
plt.close('all')