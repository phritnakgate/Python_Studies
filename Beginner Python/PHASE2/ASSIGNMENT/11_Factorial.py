#Factorial
#ปกติ
'''
import math
fac = int(input("ใส่ค่า factorial: "))
x = math.factorial(fac)
print(x)
'''
#ใช้ recursive function
fac = int(input("ใส่ค่า factorial: "))
def fact(f):
    if f == 1:
        return f
    else:
        return f * fact(f-1)
result = fact(fac)
print(fac,"!=",result)