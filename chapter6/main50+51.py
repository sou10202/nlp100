import pandas as pd
import re
from nltk import stem
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the data
colnames = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']
df = pd.read_csv('src/rawdata/newsCorpora.csv',encoding='utf-8' ,header=None, names=colnames, sep='\t')
df = df.replace(('"', "'"))
data = df[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]
# data_drop = df.index[df['PUBLISHER'].isin(['Entertainmentwise', 'atlantadailyworld', 'WSB Atlanta', 'Variety', 'Radar Online', 'Newsday', 'Hudson Hub-Times', 'HipHopDX', 'Crushable'])]
# data = data.drop(data_drop)
data = data.sample(frac=1)
data = data.reset_index(drop=True)
train_row = int(data.shape[0] * 0.8)
test_row = int(data.shape[0] * 0.1)
train = data.iloc[:train_row]
valid = data.iloc[train_row:train_row+test_row]
test = data.iloc[train_row+test_row:]

train.to_csv('src/train.txt', sep='\t', index=False)
valid.to_csv('src/valid.txt', sep='\t', index=False)
test.to_csv('src/test.txt', sep='\t', index=False)

all_data = pd.concat([train, valid, test]).reset_index(drop=True)

def preprocess_text(text):
    text_clean = re.sub(r'[\"\'.,:;\(\)#\|\*\+\!\?#$%&/\]\[\{\}]', '', text)
    # ' - 'みたいなつなぎ文字を削除
    text_clean = re.sub('\s-\s', ' ', text_clean)
    # 数字の正規化(全部0にする)
    text_clean = re.sub('[0-9]+', '0', text_clean)
    # 小文字化
    text_clean = text_clean.lower()
    # ステミングで語幹だけ取り出す
    stemmer = stem.PorterStemmer()
    res = [stemmer.stem(x) for x in text_clean.split()]
    return ' '.join(res)

all_data['TITLE'] = all_data['TITLE'].apply(preprocess_text)
vec_df = TfidfVectorizer()
x = vec_df.fit_transform(all_data['TITLE']).toarray()
x_df = pd.DataFrame(x, columns=vec_df.get_feature_names_out())
split_point = int(len(data)//3)
train_x = x_df.iloc[:split_point]
valid_x = x_df.iloc[split_point:split_point*2]
test_x = x_df.iloc[split_point*2:]
train_x.to_csv('src/train.feature.txt', sep='\t', index=False)
valid_x.to_csv('src/valid.feature.txt', sep='\t', index=False)
test_x.to_csv('src/test.feature.txt', sep='\t', index=False)

data_y = df['CATEGORY']
train_y = data_y.iloc[:split_point].to_csv('src/train.label.txt', sep='\t', index=False)
valid_y = data_y.iloc[split_point:split_point*2].to_csv('src/valid.label.txt', sep='\t', index=False)
test_y = data_y.iloc[split_point*2:].to_csv('src/test.label.txt', sep='\t', index=False)