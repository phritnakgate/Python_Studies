#โปรแกรมบัญชีธนาคา่ร
#data
account ={
    "0503140039":{
        "name":"นาย A",
        "balc":8810.00,
        "pwd":159357
    },
    "0853968137":{
        "name":"นาย B",
        "balc":598.57,
        "pwd":159357
    }
}
#ฟังก์ชั่นการทำงาน
def bankwork(num1):
    if num1 == 1:
        print("คุณมีเงิน ",account[accnum]["balc"],"บาท")
    elif num1 == 2:
        deposit()
    elif num1 == 3:
        withdrawn()
    elif num1 == 4:
        transfer()
    elif num1 == 5:
        pass
    else:
        print("ผิดพลาด กรอกใหม่")
        bankwork()
def deposit():
    try:
        checkpin = int(input("ใส่ PIN: "))
        if checkpin == account[accnum]["pwd"]:
            dep = float(input("ใส่เงินที่จะฝาก:"))
            afterdep = account[accnum]["balc"] + dep
            account[accnum]["balc"] = afterdep
            print("เงินคงเหลือ: ",account[accnum]["balc"],"บาท")
        else:
            print("PIN ผิด")
    except:
        print("ใส่ค่าผิด")
def withdrawn():
    try:
        checkpin = int(input("ใส่ PIN: "))
        if checkpin == account[accnum]["pwd"]:
            wdn = float(input("ใส่เงินที่จะถอน:"))
            if wdn > account[accnum]["balc"]:
                print("มีเงินในบัญชีไม่พอ")
            else:
                afterwdn = account[accnum]["balc"] - wdn
                account[accnum]["balc"] = afterwdn
                print("เงินคงเหลือ: ",account[accnum]["balc"],"บาท")
                tanabud(wdn)
        else:
            print("PIN ผิด")
    except:
        print("ใส่ค่าผิด")
def tanabud(money):
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
    print("คุณถอนธนบัตร 1000 ได้", thb1000, "ธนบัตร 500 ได้", thb500,"ธนบัตร 100 ได้", thb100,"ธนบัตร 50 ได้", thb50,"ธนบัตร 20 ได้", thb20,"เหรียญ 10 ได้", thb10,"เหรียญ 5 ได้", thb5,"เหรียญบาท ได้", thb1,"เหรียญ50 สตางค์ ได้", thb0_50,"เหรียญ25 สตางค์ ได้", thb0_25, "เหลือเศษ", money)
def transfer():  
        acccheck = str(input("ใส่บัญชีปลายทาง: "))
        if acccheck in account.keys():
            try:
                checkpin = int(input("ใส่ PIN: "))
                if checkpin == account[accnum]["pwd"]:
                    trans = float(input("ใส่เงินที่จะโอน: "))
                    if trans > account[accnum]["balc"]:
                            print("มีเงินในบัญชีไม่พอ")
                    else:
                        aftertrans = account[accnum]["balc"] - trans
                        account[accnum]["balc"] = aftertrans
                        aftertrans2 = account[acccheck]["balc"] + trans
                        account[acccheck]["balc"] = aftertrans2
                        print("โอนเงินสำเร็จ")
                        print("คุณเหลือเงิน ",aftertrans,"บาท")
                else:
                    print("PIN ผิด")
            except:
                print("ใส่ค่าผิด")
        else:
            print("ไม่มีเลขบัญชีนี้ในระบบ")
#MAIN PROGRAM
accnum = str(input("กรุณาใส่เลขบัญชี: "))
if accnum in account.keys():
    while True:
        print("WELCOME",account[accnum]["name"])
        work=int(input("เลือกธุรกรรม \n 1-เช็คยอดเงินในบัญชี \n 2-ฝากเงิน \n 3-ถอนเงิน \n 4-โอนเงิน \n5-ออกจากระบบ"))
        if work == 5:
            print("ขอบคุณที่ใช้บริการ")
            break
        bankwork(work)
else:
    print("ไม่มีเลขบัญชีนี้ในระบบ")