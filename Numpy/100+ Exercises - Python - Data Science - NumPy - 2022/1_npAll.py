#numpy.all functions
'''
numpy.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)[source]
Test whether all array elements along a given axis evaluate to True.
'''
import numpy as np
'''
Exercise 1
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

print("A = ",A.all()) 
print("B = ",B.all()) 
print("C = ",C.all()) 
print("D = ",D.all())

print แบบ loop
for name, array in zip(list('ABC'), [A, B, C]):
    print(f'{name}: {np.all(array, axis=1)}')
'''
#Exercise 2
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

print("A: ",np.all(A,axis=1))
print("B: ",np.all(B,axis=1))
print("C: ",np.all(C,axis=1))