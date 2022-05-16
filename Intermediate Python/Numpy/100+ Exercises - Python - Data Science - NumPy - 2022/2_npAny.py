#Any
'''
numpy.any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)[source]
Test whether any array element along a given axis evaluates to True.
'''
import numpy as np
'''
#Exercise3
A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array)}')
'''
#Exercise4
A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array,axis=0)}')