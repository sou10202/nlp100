from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd

train_x = pd.read_csv('src/train.feature.txt', sep='\t')
train_y = pd.read_csv('src/train.label.txt', sep='\t').values.ravel()
valid_x = pd.read_csv('src/valid.feature.txt', sep='\t')
valid_y = pd.read_csv('src/valid.label.txt', sep='\t').values.ravel()
test_x = pd.read_csv('src/test.feature.txt', sep='\t')
test_y = pd.read_csv('src/test.label.txt', sep='\t').values.ravel()

prams = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}
gs_model = GridSearchCV(LogisticRegression(random_state=0, max_iter=10000), prams, cv=5, verbose=1)
gs_model.fit(train_x, train_y)

best_model = gs_model.best_estimator_
print(f"正答率:{best_model.score(test_x, test_y)}")