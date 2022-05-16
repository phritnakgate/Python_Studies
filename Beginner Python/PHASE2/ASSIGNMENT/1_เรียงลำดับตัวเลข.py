#เรียงลำดับตัวเลข
number=[]
while True:
    x = int(input("ป้อนตัวเลขเต็มบวก (จบโปรแกรมให้ใส่ค่าลบ): "))
    if x < 0:
        break
    number.append(x)
number.sort()
print("เรียงจากน้อยไปมาก คือ ", number)
number.reverse()
print("เรียงจากมากไปน้อย คือ ", number)
print("จบโปรแกรม")