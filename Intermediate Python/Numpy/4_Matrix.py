#Array Matrix
'''
ใช้ความรู้ม.ปลาย
1. Square Matrix
2. Zero Matrix
3. Identity Matrix 
'''
import numpy as np
'''
วงเล็บ   () => tuple
        [] => list
'''
#Zero Matrix => ทุกตัวเป็น 0 ได้มาเป็น float
z1 = np.zeros(5,dtype='int')
print(z1)
z2 = np.zeros((3,3),dtype='int')
print(z2)

#One Matrix => ทุกตัวเป็น 1 ได้มาเป็น float
o1 = np.ones(10,dtype='int')
print(o1)
o2 = np.ones((3,3),dtype='int')
print(o2)

#Full => ข้แมูลทุกตัวเหมือนกัน
f1 = np.full(10,7)
print(f1)
f2 = np.full((3,3),5.0,dtype='int')
print(f2)

#Empty => เลขสุ่ม
e = np.empty((3,3),dtype='int')
print(e)

#Identity Matrix
iden1 = np.identity(4,dtype='int') #จัตุรัส
print(iden1)
iden2 = np.eye(4,3,2)              #m x n มิติ
print(iden2)