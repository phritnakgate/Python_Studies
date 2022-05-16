#หาตัวเลขมากน้อยUpgrade
max,min = 0, 9999
while True:
    number = float(input("ป้อนข้อมูล ถ้าหากต้องการหยุดให้พิมพ์ -1: "))
    if number < 0:
        break
    if number > max:
        max = number
    if number < min:
        min = number
print("ค่าสูงสุดคือ "+"%.2f"%max)
print("ค่าต่ำสุดคือ "+"%.2f"%min)