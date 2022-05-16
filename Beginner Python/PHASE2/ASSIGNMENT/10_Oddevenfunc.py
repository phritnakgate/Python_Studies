def oddeven(num):
    if num%2 == 0:
        print(str(num)+"เป็นเลขคู่")
    else:
        print(str(num)+"เป็นเลขคี่")
while True:
    num = float(input("ป้อนตัวเลข: "))
    oddeven(num)