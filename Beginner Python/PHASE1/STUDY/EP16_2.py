score = float(input("กรอกคะแนนของคุณ (เต็ม 100): "))
if score > 0 and score <=100:
    if score >= 80 and score <=100:
        print("คุณได้เกรด A")
    elif score >=70:
        if score >=75:
            print("คุณได้เกรด B+")
        else:
            print("คุณได้เกรด B")
    elif score >=60:
        if score >=65:
            print("คุณได้เกรด C+")
        else:
            print("คุณได้เกรด C")
    elif score <60:
        if score >= 55:
            print("คุณได้เกรด D+")
        elif score < 55 and score >=50:
            print("คุณได้เกรด D")
        else:
            print("คุณได้เกรด F")
    else:
        print("พยายามใหม่นะ")
else:
    print("ใส่คะแนน 0-100 เท่านั้น!!!")
print("จบการทำงาน")