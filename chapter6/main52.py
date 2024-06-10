from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

train_x = pd.read_csv('src/train.feature.txt', sep='\t')
train_y = pd.read_csv('src/train.label.txt', sep='\t').values.ravel()
valid_x = pd.read_csv('src/valid.feature.txt', sep='\t')
valid_y = pd.read_csv('src/valid.label.txt', sep='\t').values.ravel()
test_x = pd.read_csv('src/test.feature.txt', sep='\t')
test_y = pd.read_csv('src/test.label.txt', sep='\t').values.ravel()

model = LogisticRegression(random_state=0, max_iter=10000)
model.fit(train_x, train_y)

y_pred = model.predict(test_x)
print('===各記事のカテゴリ予測===')
print(y_pred)
y_pred_proba_test = model.predict_proba(test_x)
print('===各記事のカテゴリ予測確率===')
print(y_pred_proba_test)

y_pred_train = model.predict(train_x)
print('===学習データの正解率===')
print(accuracy_score(train_y, y_pred_train))
y_pred = model.predict(test_x)
print('===テストデータの正解率===')
print(accuracy_score(test_y, y_pred))

print('===学習データの混同行列===')
print(confusion_matrix(test_y, y_pred))
print('===テストデータの混同行列===')
print(confusion_matrix(test_y, y_pred))

print('===学習データの適合率===')
print(precision_score(test_y, y_pred, average=None))

print(f'[カテゴリ順]{model.classes_}')
print(f'[適合率]{precision_score(test_y, y_pred, average=None)}')
print(f'[再現率]{recall_score(test_y, y_pred, average=None)}')
print(f'[F1スコア]{f1_score(test_y, y_pred, average=None)}')

print('===マクロ平均===')
print(f'[適合率]{precision_score(test_y, y_pred, average="macro")}')
print(f'[再現率]{recall_score(test_y, y_pred, average="macro")}')
print(f'[F1スコア]{f1_score(test_y, y_pred, average="macro")}')
print('===マイクロ平均===')
print(f'[適合率]{precision_score(test_y, y_pred, average="micro")}')
print(f'[再現率]{recall_score(test_y, y_pred, average="micro")}')
print(f'[F1スコア]{f1_score(test_y, y_pred, average="micro")}')

features = train_x.columns.values
for i in range(len(model.classes_)):
    importance = model.coef_[i]
    feature_importance = [(features[j], np.abs(importance[j])) for j in range(len(importance))]