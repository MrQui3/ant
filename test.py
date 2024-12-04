import numpy as np


a = np.array([[3, 4, 4, 5], [1, 2, 4, 6]])
a = np.append(a, [[5]], axis=1)
print(a)