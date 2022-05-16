#Allclose
'''
numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
Returns True if two arrays are element-wise equal within a tolerance.
'''
import numpy as np
A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])
print(np.allclose(A,B))