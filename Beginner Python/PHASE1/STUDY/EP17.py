#คำสั่ง pass ใช้กับการข้าม statement ในกรณีที่เราวางโครงสร้างไว้ไม่รู้จะใส่ statement อะไร
age=int(input("กรอกอายุ: "))
gender=(input("เพศ(ชาย M หญิง F): "))
if age>=15 and age <=150:
    if gender == "M":
      print("สวัสดี นาย ")  
    elif gender == "F":
        print("สวัสดี นางสาว ")
    else:
        print("กรอกข้อมูลผิด ไปกรอกใหม่ซะ!")
else:
    if gender == "M":
      pass 
    elif gender == "F":
        pass
    else:
        pass
print("จบการทำงาน")