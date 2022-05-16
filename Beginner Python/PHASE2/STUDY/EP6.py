#Non-Primitive : List, Tuple, Dict, Set
#Dict
#1. construct => key(เข้าถึงข้อมูล),value(ค่าของข้อมูล) => key:value ใช้ {}
grade = {
    "A": "very good",
    "B": "good",
    "C": "fair",
    "D": "poor"
}
print(grade)
dorm = dict({101:"นาย A", 102:"นาย B", 103:"นาย C"})

#2. เข้าถึงข้อมูล
print(dorm[101])
print(dorm.get(102))

#3. เปลี่ยนข้อมูล
dorm[103] = "K.ปังปอนด์"
print(dorm[103])

#4. เพิ่มข้อมูล
dorm.update({104:"ว่าง",105:"กำลังทำสัญญา"})
print(dorm)

#5. แสดงผล loop for
for item in dorm.values():
    print(item)
for item2 in dorm.keys():
    print(item2)
for k,v in dorm.items():
    print("Room",k,"Vaccancy",v)

#6. ลบ
dorm.update({106:"ว่าง",107:"กำลังทำสัญญา"})
print(dorm)
dorm.popitem()      #ลบตัวท้ายสุด
print(dorm)
dorm.pop(106)       #ลบ dict นั้นๆ
print(dorm)
grade.clear()       #ลบสมาชิก
print(grade)
del grade           #ลบตัวแปร

#7. คัดลอก dict
dorm2 = dorm.copy()
print(dorm2)

#8. Dict ซ้อน Dict
market = {
    "ร้านป้าพร": {
        "name":"ป้าพร",
        "menu":["อาหารตามสั่ง","ก๋วยเตี๋ยว"],
        "zone":"A"
    },
    "ร้านลุงป้อม": {
        "name":"อีป้อม",
        "menu":["Apple","Banana"],
        "zone":"A"
    },
    "ร้านน้าใจ": {
        "name":"เจ๊ใจ",
        "menu":["นมปั่น","ชาร้อน"],
        "zone":"B"
    }
}
print(market)
print(market["ร้านป้าพร"]["menu"])