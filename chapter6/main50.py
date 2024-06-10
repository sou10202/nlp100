import pandas as pd

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
print()