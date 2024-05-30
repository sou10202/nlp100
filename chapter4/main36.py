import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

data = pd.read_csv('out/word_count.csv', encoding='utf-8')
# plt.rcParams['font.family'] = 'Ms Gothic' 
data[:10].plot.bar(x = 'word')
plt.savefig('out/count_words.png')
plt.close('all')