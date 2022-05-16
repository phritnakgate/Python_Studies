#ค้นหาเบอร์โทรศัพท์
emerg = {
    191:"police",
    1669:"sick",
    199:"fire",
    1163:"siengtung"
}
def searchnumber(message):
    for key,value in emerg.items():
        if value == message:
            print("เบอร์คือ",key)
        else:
            print("ไม่พบข้อมูล")
            return
searchnum = str(input("ใส่ key เบอร์ฉุกเฉิน: "))
searchnumber(searchnum)