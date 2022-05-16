import numpy as np
#1 มิติ
a = np.arange(10)
print(a.sum())
print(a.prod())
print(a.max())
print(a.argmax())
print(a.min())
print(a.argmin())
print(a.mean())
#2 มิติ
b = np.array([[10,20,30],[40,50,90],[80,100,5]])
print(np.min(b,axis=1))     #แนวนอน
print(np.min(b,axis=0))     #แนวตั้ง