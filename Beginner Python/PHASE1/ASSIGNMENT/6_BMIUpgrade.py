#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย) แบบแปลผลได้
#BMI = น้ำหนัก (kg) / ส่วนสูง (m) ยกกำลัง 2

print("ยินดีต้อนรับสู่โปรแกรมคำนวณดัชนีมวลกาย(BMI)")
weight=float(input("กรุณากรอกน้ำหนัก(kg): "))
height=float(input("กรุณากรอกส่วนสูง(cm): "))/100

BMI = weight / (height**2)
BMIoutput = "BMI ของคุณคือ {:.2f}"

print(BMIoutput.format(BMI))
if BMI >= 0 and BMI < 18:
    print("ผล: ต่ำกว่าเกณฑ์")
elif BMI >= 18.5 and BMI <= 22.9:
    print("ผล: สมส่วน")
elif BMI >= 23 and BMI <= 24.9:
    print("ผล: น้ำหนักเกิน")
elif BMI >= 25 and BMI <= 29.9:
    print("ผล: โรคอ้วนระดับที่ 1")
elif BMI >30:
    print("ผล: โรคอ้วนระดับอันตราย")
else:
    print("กรุณาใส่ค่าที่ถูกต้อง")
print("จบการทำงาน")