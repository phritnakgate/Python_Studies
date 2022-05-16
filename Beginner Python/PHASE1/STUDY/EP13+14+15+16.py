"""
Control Structure
1. แบบลำดัย
2. แบบเลือก
3. แบบทำซ้ำ
"""
#แบบเลือก => if-else อย่าลืม tab คำสั่งทุกครั้ง และใส่ ":" ด้วย
name=(input("กรอกชื่อ: "))
age=int(input("กรอกอายุ: "))
gender=(input("เพศ(ชาย M หญิง F): "))
#Ternary Operator
print("บรรลุนิติภาวะ") if age>=20 else print("ยังไม่บรรลุนิติภาวะ")

if age>=15 and age <=150:
    if gender == "M":
      print("สวัสดี นาย ", name)  
    elif gender == "F":
        print("สวัสดี นางสาว ", name)
    else:
        print("กรอกข้อมูลผิด ไปกรอกใหม่ซะ!")
elif age >0 and age <15:  
    if gender == "M":
        print("สวัสดี ด.ช. ", name)
    elif gender == "F":
        print("สวัสดี ด.ญ. ", name)
    else:
        print("กรอกข้อมูลผิด ไปกรอกใหม่ซะ!")
else:
    print("กรอกข้อมูลผิด ไปกรอกใหม่ซะ!")
print("จบโปรแกรม")


