from tqdm import tqdm
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

train_x = pd.read_csv('src/train.feature.txt', sep='\t')
train_y = pd.read_csv('src/train.label.txt', sep='\t').values.ravel()
valid_x = pd.read_csv('src/valid.feature.txt', sep='\t')
valid_y = pd.read_csv('src/valid.label.txt', sep='\t').values.ravel()
test_x = pd.read_csv('src/test.feature.txt', sep='\t')
test_y = pd.read_csv('src/test.label.txt', sep='\t').values.ravel()

result = []
for c in tqdm(np.logspace(-4, 2, 10, base=10)):
    model = LogisticRegression(random_state=0, max_iter=10000, C=c)
    model.fit(train_x, train_y)

    train_pred = model.predict(train_x)
    valid_pred = model.predict(valid_x)
    test_pred = model.predict(test_x)

    train_accuracy = accuracy_score(train_y, train_pred)
    valid_accuracy = accuracy_score(valid_y, valid_pred)
    test_accuracy = accuracy_score(test_y, test_pred)
    result.append([c, train_accuracy, valid_accuracy, test_accuracy])

fig , ax = plt.subplots()
result = np.array(result)
ax.plot(result[:,0], result[:,1], label='train')
ax.plot(result[:,0], result[:,2], label='valid')
ax.plot(result[:,0], result[:,3], label='test')
ax.set_xscale('log')
ax.set_xlabel('C')
ax.set_ylabel('Accuracy')
ax.legend()
plt.savefig('result58.png')
