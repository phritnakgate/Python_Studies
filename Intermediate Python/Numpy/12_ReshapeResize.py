import numpy as np
#reshape
a = np.arange(10)
print(a.reshape(2,5))

#flatten => จัดให้เหลือ 1 มิติ แล้ว return กลับเป็น array ตัวเดิม ไม่สามารถแก้ข้อมูลได้เมื่อเก็บไว้ในตัวแปรตัวใหม่
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = b.flatten()
c[0] = 10
print(c)
print(b)

#ravel => เหมือน flatten แต่สามารถแก้ข้อมูลได้เมื่อเก็บไว้ในตัวแปรตัวใหม่
d = b.ravel()
d[4] = 55
print(d)
print(b)