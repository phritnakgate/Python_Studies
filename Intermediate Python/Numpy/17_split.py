import numpy as np
a = np.arange(1,21)
print(a)
print(np.split(a,4))
a = a.reshape(5,4)
print(np.hsplit(a,4))  #แนวตั้ง
print(np.vsplit(a,5))  #แนวนอน