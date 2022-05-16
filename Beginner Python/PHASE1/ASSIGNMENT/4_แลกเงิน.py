#แลกเงินและคำนวณจำนวนธนบัตร+เหรียญ (เลือกจำนวนธนบัตร/เหรียญไม่ได้)
money = float(input("ป้อนจำนวนเงินเพื่อแลก: "))
print("จากเงินทั้งหมด", money , "บาท คุณแลกได้")
if money > 0:
    thb1000 = money//1000
    money = money - (thb1000*1000)
    thb500 = money//500
    money = money - (thb500*500)
    thb100 = money//100
    money = money - (thb100*100)
    thb50 = money//50
    money = money - (thb50*50)
    thb20 = money//20
    money = money - (thb20*20)
    thb10 = money//10
    money = money - (thb10*10)
    thb5 = money//5
    money = money - (thb5*5)
    thb1 = money//1
    money = money - (thb1*1)
    thb0_50 = money//0.5
    money = money - (thb0_50*0.5)
    thb0_25 = money//0.25
    money = money - (thb0_25*0.25)
    print("คุณแลกธนบัตร 1000 ได้", thb1000, "ธนบัตร 500 ได้", thb500,"ธนบัตร 100 ได้", thb100,"ธนบัตร 50 ได้", thb50,"ธนบัตร 20 ได้", thb20,"เหรียญ 10 ได้", thb10,"เหรียญ 5 ได้", thb5,"เหรียญบาท ได้", thb1,"เหรียญ50 สตางค์ ได้", thb0_50,"เหรียญ25 สตางค์ ได้", thb0_25, "เหลือเศษ", money)
else:
    print("จำนวนเงินผิดพลาด")
print("จบการทำงาน")