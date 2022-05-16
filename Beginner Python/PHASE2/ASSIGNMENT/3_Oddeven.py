#Odd Even
number=[]
odd=[]
even=[]
while True:
    x = int(input("ป้อนตัวเลขเต็มบวก (จบโปรแกรมให้ใส่ค่าลบ): "))
    if x < 0:
        break
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)
    number.append(x)
print("เลขคู่ ได้แก่", even)
print("เลขคี่ ได้แก่", odd)