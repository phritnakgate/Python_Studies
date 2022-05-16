import numpy as np


A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])
print(A == B)

C = np.array([0.4, 0.5, 0.3, 0.9])
D = np.array([0.38, 0.51, 0.3, 0.91])
print(C > D)