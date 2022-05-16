#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
#BMI = น้ำหนัก (kg) / ส่วนสูง (m) ยกกำลัง 2

print("ยินดีต้อนรับสู่โปรแกรมคำนวณดัชนีมวลกาย(BMI)")
weight=float(input("กรุณากรอกน้ำหนัก(kg): "))
height=float(input("กรุณากรอกส่วนสูง(cm): "))/100

BMI = weight / (height**2)

print("BMI ของคุณคือ ",BMI)