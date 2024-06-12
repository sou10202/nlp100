import numpy as np

result = [[1, 0.1, 0.2, 0.3], [2, 0.2, 0.3, 0.4], [3, 0.3, 0.4, 0.5]]
x = np.logspace(-4, 2, 10, base=10)
result = np.array(result)
print(result[:,0])
print(x)