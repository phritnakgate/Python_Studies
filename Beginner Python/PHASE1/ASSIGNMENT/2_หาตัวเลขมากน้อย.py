#หาตัวเลขมาก/น้อย
a = float(input("ป้อนตัวเลขตัวที่ 1: "))
b = float(input("ป้อนตัวเลขตัวที่ 2: "))

if a > b:
    print(a,"มากกว่า",b)
elif a==b:
    print(a,"เท่ากับ",b)
else:
    print(a,"น้อยกว่า",b)
print("จบการทำงาน")