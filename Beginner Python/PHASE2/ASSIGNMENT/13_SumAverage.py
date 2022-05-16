#หาผลรวม/ค่าเฉลี่ย โดยใช้ list
x = []
while True:
    a = float(input("ใส่ค่าของคุณ หยุดให้ใส่ค่า -1: "))
    if a < 0:
        break
    else:
        x.append(a)
print("ค่าที่กรอก คือ \n",x)
check = input("ค่าถูกหรือไม่ (Y/N): ")
if check == "Y":
    length = len(x)
    summation = sum(x[0:])
    average = summation / length
    print("ผลบวก คือ ",summation,"ค่าเฉลี่ย คือ",average)
elif check == "N":
    editpos = int(input("ต้องการแก้ค่าตำแหน่งไหน (เริ่มจาก 0): "))
    if editpos < 0 or editpos > len(x):
        print("กรอกค่าผิด")
    else:
        editdata = float(input("ใส่ค่าของคุณ: "))
        x[editpos]=editdata
        length = len(x)
        summation = sum(x[0:])
        average = summation / length
        print("ผลบวก คือ ",summation,"ค่าเฉลี่ย คือ",average)
else:
    print("กรอกค่าผิด")
