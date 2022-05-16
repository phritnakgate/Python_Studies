#Function
#1. ทำไมเราต้องเขียน function?
a,b,c=10,23,40
'''
เช็คเคส 3 เคสที่คำสั่งซ้ำกัน เยอะมากกกกก บรรทัดก็เยอะ รวบไปเลยดีกว่า
if a%2 == 0:
    print("เลขคู่")
else:
    print("เลขคี่")
if b%2 == 0:
    print("เลขคู่")
else:
    print("เลขคี่")
if c%2 == 0:
    print("เลขคู่")
else:
    print("เลขคี่")
'''

#2. การสร้างและเรียก function
'''
def ชื่อฟังก์ชั่น():
    statement
'''
def sayhi():                    #สร้าง function
    print("HELLO WELCOME Eiei")
sayhi()                         #เรียกใช้งาน function
def add():
    x = 3+1
    print(x)
for i in range(4):
    add()

#3. Global Variable และ Local Variable
def displaynumber():
    e=10    #Local Variable
    print("Hello = ",e)
e = 20      #Global Variable
displaynumber()
print("Hello = ",e)

#4. การรับค่าเข้ามาใน function
'''
def plus(num1,num2):
    print(str(num1)+"+"+str(num2)+"=",num1+num2)
num1=int(input("ใส่เลขแรก: "))
num2=int(input("ใส่เลขหลัง: "))
result = plus(num1,num2)
print(result)
'''
#5. Arguments Parameter
'''
Arguments => ค่าที่ส่งเข้าไปใน function
Parameter => ค่าตัวแปรที่รับข้อมูลมาทำงาน
Ar ส่ง Pa รับ
'''

#6. Arbitrary Arguments => agrs 
'''
ใช้เมื่อ function ประเภทเดียวกันแต่มีการซ้ำซ้อนของ parameter
เช่น บวกเลข 2 ตัว 3 ตัว เขียน function แบบเดียวกัน แต่ parameter ไม่เท่ากัน
'''
def add(*agrs):
    print(sum(agrs))
add()
add(10)
add(10,20)
add(10,20,30)

#7. Keyword Arguments
def displayData(fname,lname,city):
    print("ชื่อจริง: ",fname)
    print("นามสกุล: ",lname)
    print("จังหวัดที่อาศัยอยู่",city)
displayData("หาดใหญ่","ปริชญ์","นาคเกตุ") #ข้อมูลใส่เรียง parameter!
displayData(city="หาดใหญ่",fname="ปริชญ์",lname="นาคเกตุ") #เอาค่าไปใส่ให้ถูก parameter

#8. Default Parameter 
'''
ไว้กำหนดค่าพื้นฐานของ parameter
เช่น def displayData(fname,lname,city="bangkok")
'''

#9. List/Tuple Parameter
def displayFruit(item):
    for loo in range(len(item)):
        print("ผลไม้ชิ้นที่",loo+1,"คือ",item[loo])
fruit=["ผลไม้","มะม่วง","มะละกอ"]
displayFruit(fruit)
fruit2=("apple","strawberry")
displayFruit(fruit2)

#10. รับค่าและส่งกลับ => return / Return เปล่าๆ => กระโดดออกจาก function
def minus(numm1,numm2):
    return numm1-numm2
print(minus(b,a))
'''
def lottery(huay):
    if len(huay)<6:
        print("ใส่ค่าผิด")
        return
    if huay == "395919":
        print("ถูกหวย")
        return 6000000
    else:
        print("ไม่ถูกหวย")
        return 0
huayprice = 80
money = 100
huay = input("ใส่เลขหวย: ")
polhuay = lottery(huay)
money -= huayprice
print("รางวัลที่ได้: ",polhuay)
print("เงินคงเหลือ: ",polhuay+money)
'''
#สรุปรูปแบบ function
'''
สรุป function มี 4 รูปแบบ
1. ไม่มีการรับและส่งค่า
def name():
    <คำสั่ง>

2. มีการรับค่าเข้าไปทำงานอย่างเดียว
def name(parameter1,parameter2,...):
    <คำสั่ง>

3. มีการส่งค่าอย่างเดียว
def name():
    <คำสั่ง>
    return <value>

4. มีการรับค่าเข้าไปทำงานและส่งค่า
def name(parameter1,parameter2,...):
    <คำสั่ง>
    return <value>
'''
#11. Arbitrary Arguments => kwargs 
def displayData2(**kwargs):
    print(kwargs)
    print(kwargs["fname2"])
displayData2(fname2 = "Phrit",lname2 = "Nakgate",nname = "Boss", age = 18, city2="Hadyai")
displayData2(fname2 = "Noppawich",lname2 = "Saelee",nname = "Fuse", age = 18, city2="Hadyai")

#12. Function เรียก function
def equal(e1,e2,e3):
    return compareMax(compareMax(e1,e2),e3)
def compareMax(com1,com2):
    if com1>com2:
        return com1
    else:
        return com2
maxx = equal(10,5,-2)
print("ค่ามากสุด: ",maxx)

#13. Recursive Function => เรียก function ตัวเอง
'''
1. หาจุดวนซ้ำ
2. หาจุดออกจาก function (return)
3. ต้องมี parameter
'''
def A(AA):
    if AA == 10:
        return
    else:
        print(AA)
        AA+=1
        A(AA)
A(0)
def B(BB):
    if BB == 1:
        return BB
    else:
        return BB+B(BB-1)
hehe = B(5)
print(hehe)

#14. Pass => ร่าง function ไว้ก่อน
def getCity():
    pass

#15. Lambda function => ไม่อยากให้มีชื่อ function
'''
lambda arguments : expression
'''
sumss=lambda s1,s2 : s1+s2
print(sumss(5,10))
def mypower(oh):
    return lambda ohoh : oh**ohoh
yyy = mypower(5)
ress=yyy(2)
print(ress)