#การสร้างArray
import numpy as np
#0 มิติ
arr0 = np.array(2)          
print(arr0)
print(arr0.ndim)            #เช็คมิติ array

# 1 มิติ
arr1 = np.array([1,2,3])    #1 มิติ  
print(arr1)
print(arr1.ndim)
li = [1,2,3,4]
arrl = np.array(li)         #สร้างจาก list
print(arrl)
tup = (1,2,3,4,5,6,7,8,9,10)#สร้างจาก tuple
arrtup = np.array(tup)         #สร้างจาก list
print(arrtup)

# 2 มิติ
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
print(arr2.ndim)

# 3 มิติ
arr3 = np.array([[[1,2,3],[4,5,6]]])
print(arr3)
print(arr3.ndim)