#เกมทายเลขลูกเต๋า
from random import randrange
dice = int(randrange(1,7)) #1-6
print("ตอบหน้าลูกเต๋าได้ 3 ครั้งนาจา")
k = 1
kout = 3
while True:
    number = int(input("สุ่มสิจ๊ะ: "))
    if number < 0 or number > 6:
        print("ลูกเต๋ามีแค่หน้า 1-6 ไปใส่ใหม่ไป๊")
        break
    else:
        if k ==3:
            print("ว้า แย่จังเดาผิด คำตอบคือ ", dice)
            break
        elif number == dice:
            print("เดาถูก เย่ะ")
            break
        else:
            kout-=1
            print("เดาใหม่ เย่ะ เหลืออีก ", kout, "ครั้ง")
            if number > dice:
                print("เยอะปายยย")
            else:
                print("น้อยปายยยย")
            number = 0
            k+=1
            continue