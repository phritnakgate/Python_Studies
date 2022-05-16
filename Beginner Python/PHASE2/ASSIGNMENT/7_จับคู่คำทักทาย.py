#จับคู่คำทักทาย
greet = ["หวัดเด", "Hello", "Good Bye", "ลาก่อย"]
name = ["ก้อง", "แก้ม"]
result=[]

#ปกติ
for x in greet:
    for y in name:
        result.append(x+y)
print(result)

'''
#ลดรูป
result = [x+y for x in greet for y in name]
'''