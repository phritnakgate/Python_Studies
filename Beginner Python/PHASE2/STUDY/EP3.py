#Non-Primitive : List, Tuple, Dict, Set
#Set

#1. Constructor => ใช้ {}
day_set = {'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}
print(day_set)
print(type(day_set))
fish = set(['ปลาดุก','ปลาหมอ','ปลาดุก'])
print(fish)
fruit=["มะม่วง","มะขาม","มะยม"]
print(type(fruit))
sfruit = set(fruit)
print(sfruit)

#2. เพิ่มข้อมูล
#ทีละตัว => add
sfruit.add("ทุเรียน")
sfruit.add("สับปะรด")
print(sfruit)
#หลายตัว => update
tomyum=['ตะไคร้', 'หัวหอม']
sfruit.update(tomyum)
print(sfruit)

#3. Loop
for item in day_set:
    print("วัน",item)

#4. แสดงจำนวนสมาชิกในเซต
print(len(day_set))

#5. เช็คข้อมูล
print("Friday" in day_set)
print("monday" in day_set)

#6. ลบข้อมูล
#remove
fish.remove("ปลาดุก")
print(fish)
#discard => มีไม่มีข้อมูลก็ได้ ลบก็ต่อเมื่อมีสมาชิก
sfruit.discard("มะยม")
print(sfruit)
fish.discard("ปลาดุก")
print(fish)
fish.clear() #ล้างข้อมูล
print(fish)
del fish    #ลบตัวแปรแม่งเลอ