#เติม-ลบสมาชิก
import numpy as np
a = np.array([3,4,2,6])
b = np.array([8,6,5,10])
print(np.concatenate((a,b))) #รวม a b
print(np.append(a,500))     #ไม่ได้ assign ค่าลงไป ถ้าจะให้ assign ให้กำหนดค่าลงไป
c = np.array([[1,2],[3,4]])
print(np.insert(c,1,100,axis=0))
print(np.insert(c,1,100,axis=1))
d = np.arange(1,11)
print(np.delete(d,2))
print(np.delete(c,1,axis=1))