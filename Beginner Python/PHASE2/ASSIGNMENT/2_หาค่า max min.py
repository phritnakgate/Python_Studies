#หาค่า max min
number=[]
while True:
    x = int(input("ป้อนตัวเลขเต็มบวก (จบโปรแกรมให้ใส่ค่าลบ): "))
    if x < 0:
        break
    number.append(x)
print("น้อยที่สุด คือ ", min(number))
print("มากที่สุด คือ ", max(number))
print("จบโปรแกรม")