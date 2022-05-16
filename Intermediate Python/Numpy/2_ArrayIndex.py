#การเข้าถึงข้อมูลใน array(index) => คล้าย python ปกติ
import numpy as np
#1 มิติ
arr = ([1,2,3,4,5])
print(arr[2])
print(arr[-2])
#2 มิติ =>index แบบลบกลับข้างเอา [row][column]
arr2 = ([[1,2,3],[10,20,30],[7,8,9]])
print(arr2[2][2])
#3 มิติ [depth][row][column]
arr3 = ([[[1,2,3],
          [4,5,6]]])
print(arr3[0][0][0])
arr3_2 = ([[[1,2,3],
            [4,5,6]],
            [[7,8,9],
            [10,11,12]]])
print(arr3_2[1][0][1])