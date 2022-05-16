#NumPyAttribute
'''
เช่น
1.ndim  => บอกจำนวนมิติของ array
2.dtype => บอกชนิดข้อมูลของ array
3.shape => บอกลักษณะของ array
4.size  => บอกขนาดของ array
5.itemsize  => หาขนาด byte 1 byte = 8 bit
'''
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
def att(arr):
    print(arr.ndim)
    print(arr.dtype)
    print(arr.shape)
    print(arr.size)
    print(arr.itemsize)
att(arr1)
att(arr2)