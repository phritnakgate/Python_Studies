#Non-Primitive : List, Tuple, Dict, Set
#List
'''
เขียนแบบ primitive เช่น
a0 = 1
a1 = 2
a2 = 3
a3 = 4
a4 = 5
เปลืองพท.หน่วยความจำจาดๆ ใช้ non-primitive ดีกว่า
'''
#1. การนิยาม
num = []            #List ว่าง
a = [1,2,3,4,5]

#2. constructor
name=list(["นาย ก", "นาย ข"])
print(name)

#3.เข้าถึงข้อมูล
print(a[2])

#4.แก้ไขข้อมูล ชื่อตัวแปร[index] = ข้อมูลที่แก้ไข
fruit = ["apple","orange","kiwi","grape","banana"]
fruit[0] = "cherry"
fruit[4] = "apple"
print(fruit)

#5.แสดงผลด้วย loop
for x in fruit:
    print(x)

#6.ตรวจสอบข้อมูล
if 'orange' in fruit:
    print("มีส้ม")
else:
    print("ไม่มีส้ม")

#7. นับจำนวนสมาชิก (len) และทำงานกับ loop for
print(len(fruit))
for i in range(len(fruit)):
    print(fruit[i])

#8. การเพิมช้อมูล => append insert
fruit.append("strawberry")
print(fruit)
fruit.insert(1,"durian")
print(fruit)

#9. การลบข้อมูล => remove pop del clear
fruit.remove("kiwi")
print(fruit)
fruit.pop()
print(fruit)
del fruit[0]
print(fruit)
fruit.clear()
print(fruit)

#10. คัดลอกข้อมูล
fruit.append("mangoooooo")
fruity = fruit.copy()
print(fruity)

#11. รวมข้อมูล(+ และ extend)
alldata = a + fruity
print(alldata)
a.extend(fruit)
print(a)

#12. แสดงจำนวนสมาชิก => count
num2 = [1,2,3,4,5,5,10,6,7,8,10,9]
j = num2.count(5)
print(j)