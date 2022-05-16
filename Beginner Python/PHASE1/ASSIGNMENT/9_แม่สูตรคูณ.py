#แม่สูตรคูณ
mom1 = int(input("ใส่จุดเริ่มแม่สูตรคูณที่ต้องการ: "))
mom2 = int(input("ใส่จุดเริ่มแม่สูตรคูณที่ต้องการ: "))
if mom1 > 0 and mom2 > 0:
    for x in range(mom1,mom2+1):
        print("แม่ ", x)
        for y in range (1,13):
            print (x, "x", y , "=", (x*y))
else:
    print("กรุณาใส่ค่าที่ถูกต้อง")