#สร้างภาพวาดสี่เหล่ยมจัตุรัส+ขอบ
'''
สี่เหลี่ยมเต็ม
number=int(input("ป้อนขนาด = "))
for row in range(number):
    for column in range(number): 
        print("X", end="")
    print(" ") #บรรทัดใหม่
'''
#ข้างในกลวง
number=int(input("ป้อนขนาด = "))
for row in range(number):
    for column in range(number): 
        if row == 0 or row==number-1 or column == 0 or column == number - 1:
            print("X", end="")
        else:
            print(" ", end="") #ช่องว่างคั่นกลางขอบ
    print(" ") #บรรทัดใหม่