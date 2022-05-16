#Type Conversion => ex int(z) แปลงใช้ในบรรทัดนั้นเท่านั้น
x = 10
y = 20.58
z = "30"
result = x+y
#string => int
result_2 = x + int(z)
result_3 = y + float(z)

#แปลงถาวร เช่น z = float(z) ใส่ในบรรทัดบน
print(x)
print(float(x))
print(type(x))
print(y)
print(int(y))
print(type(y))
print(result)
print(result_2)
print(result_3)