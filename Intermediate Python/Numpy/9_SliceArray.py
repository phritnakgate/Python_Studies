#Slice Array
#1 มิติ
import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1[2:])
print(arr1[:5])
print(arr1[1:5])
print(arr1[1:9:2])
print(arr1[::2])

#2 มิติ => [start,stop,step (row), start,stop,step (column)]
arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr2[1:,1:])
print(arr2[:,2:])
print(arr2[1:,:])
print(arr2[1:2,1:2])