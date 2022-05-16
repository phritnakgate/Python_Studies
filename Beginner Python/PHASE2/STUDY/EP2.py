#Non-Primitive : List, Tuple, Dict, Set
#Tuple

#1. การนิยาม => ใช้ ()
num = (111,222,333,111,222,222,333)
print(num)
print(type(num))

#2. constructor
color = ("red", "green", "blue", "pink")
print(color)
city = ("สุวรรณภูมิ", "หาดใหญ่", "ดอนเมือง", "เชียงใหม่")

#3. เข้าถึงข้อมูล
print(color[2])
print(color[0:2]) #index 0 ถึง ก่อน 2
print(color[1:])  #index 1 ถึง สุดท้าย
print(color[:2])  #ก่อน index 2

#4. แก้ไขข้อมูล => แปลงเป็น list
lnum = list(num)
lnum[3]=444
num=tuple(lnum)
print(num)

#5. แสดงผลด้วย loop
for item in color:
    print(item)

#6. ตรวจสอบข้อมูล
if 222 in num:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")

#7. นับจำนวนสมาชิก => len
print(len(color))
for items in range(len(color)):
    print(color[items])

#8. สร้างและเพิ่มข้อมูล (Join)
new = (555,666)
num+=new
print(num)

#9. ทำงานร่วมกับ list
airport = ["bkk", "hdy", "dmk", "cnx"]
city = city + tuple(airport) 
print(city)
lis = list(city)
#ลบข้อมูล
lis.pop()
lis.remove("เชียงใหม่")
print(lis)

#10. ค้นหาและนับจำนวนสมาชิก (count)
x = num.count(222)
print(x)
airt = tuple(airport)
yyy = airt.index("dmk")
print(yyy)

#11. Sort ข้อมูล
eiei = (100,99,88,50,200,1,2,3,4,3.99,4)
print(eiei)
ei = list(eiei)
ei2 = list(eiei)
ei.sort()
ei2.reverse()
eiei = tuple(ei)
eiei2 = tuple(ei2)
print(eiei)
print(eiei2)

#12. นำค่าใน tuple ใส่ในตัวแปร
tup=(10,20,30)
k,l,m = tup
print(k,l,m)

#13. สลับ tuple
oh1=(50,60)
oh2=(88,99)
oh1,oh2=oh2,oh1
print(oh1)
print(oh2)

#14. tuple => string
nick = ('b','o','s','s')
nickname="".join(nick)
print(nickname)

#15. reverse
rev = (100,20,30,15,10,5,500)
re = reversed(rev)
print(tuple(re)) 