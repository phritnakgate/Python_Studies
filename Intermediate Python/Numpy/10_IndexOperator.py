import numpy as np
#1 มิติ
x = np.arange(1,10)
inde = np.array([1,5,7])
print(x[inde])
print(x[[1,4,1,4,1,4]])

#2 มิติ => [row,column]
arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr2[[0,1,2],[0,1,2]])

#การทำงานกับเครื่องหมายทางคณิตศาสตร์
arr3 = np.array([[1,-2,-3],
                  [4,-5,-9]])
print(arr3[arr3<0])