'''
เจาะลึก String #1: 
1. index => index แบบบวก เริ่มที่ 0 index แบบลบ เริ่มที่ -<ความยาว string>
'''

print("Hello"[0])
print("Hello"[4])
print("Hello"[-5])
print("Hello"[-1]) 
print("Hello"[-2:]) # : คือ ตั้งแต่__ถึงจุดสุดท้าย
print("Hello"[5:])
print(len("Hello"))

'''2. ลบช่องว่างซ้ายขวา'''
#ลบช่องว่างซ้ายขวา
name = " boss "
print(len(name))
name=name.strip()
print(len(name))
name2 = " boss2 "
#ลบช่องว่างซ้าย
name2.lstrip()
print(len(name))
#ลบช่องว่างขวา
name2.rstrip()
print(len(name))

'''3. แปลง case'''
name3 = "boSs"
print(name3.upper())
print(name3.lower())
print(name3.capitalize())

'''4. การแทนที่'''
name4 = "go shopping at siam paragon paragon"
name5 = name4.replace("paragon", "center", 2)
print(name5)

'''5. การเช็คข้อความ'''
check = "paragon" in name4
print(check)
check2 = "center" in name4
print(check2)
