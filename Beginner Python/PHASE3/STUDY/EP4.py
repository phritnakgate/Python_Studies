#Utility Module

#1. Date and Time
'''
https://docs.python.org/3/library/datetime.html?highlight=date#module-datetime
'''
import datetime
result = datetime.datetime.now()    #วันเวลาปัจจุบัน
print(result.year)                  #ปี
print(result.month)                 #เดือน
newdate = datetime.datetime(2022,4,28)
#รูปแบบการแสดงผล
print(result.strftime("%x"))    #m/d/y สั้น
print(result.strftime("%X"))    #เวลา
print(result.strftime("%c"))    #m/d/y วัน-เวลา ยาว
print(result.strftime("%H:%M:%S %p"))    #hour minute second AM/PM
print(result.strftime("%j"))    #ลำดับที่เท่าใดของปี
print(result.strftime("%a"))    #วันแบบย่อ
print(result.strftime("%A"))    #วัน
print(result.strftime("%w"))    #วันที่เท่าใดของสัปดาห์ 0-sunday
print(result.strftime("%d"))    #วันที่
print(result.strftime("%b"))    #เดือนแบบย่อ
print(result.strftime("%B"))    #เดือนแบบเต็ม
print(result.strftime("%m"))    #เลขเดือน
print(result.strftime("%Y"))    #ปี ค.ศ

#2. Math
'''
จำนวนจริง
https://docs.python.org/3/library/math.html?highlight=math#module-math
จำนวนเชิงซ้อน
https://docs.python.org/3/library/cmath.html?highlight=math#module-cmath
'''
import math
print(min(1,2,3,4,5))   #หาค่าต่ำสุด
print(max(1,2,3,4,5))   #หาค่าสูงสุด
print(abs(-50))         #ค่าสัมบูรณ์
print(pow(5,2))         #ยกกำลัง
print(math.sqrt(64))    #รากที่ 2
print(math.floor(80.4)) #ปัดเศษลง
print(math.ceil(80.4))  #ปัดเศษขึ้น
print(math.pi)          #ค่าคงที่ pi
print(math.log10(2))    #log2
#ฟังก์ชั่นตรีโกณ
print("%.2f"%math.sin(math.pi/6))  #sin
print("%.2f"%math.cos(math.pi/6))  #cos
print("%.2f"%math.tan(math.pi/6))  #tan
#เรขาคณิตวิเคราะห์
point1 = [2,5]
point2 = [7,4]
result2 = math.dist(point1,point2)  #ระยะห่างจุดกับจุด
print(result2)

#3. Random
'''
https://docs.python.org/3/library/random.html?highlight=random#module-random
'''
import random
'''
random.random สุ่มเลข
random.uniform(min,max) สุ่มเลขมีช่วง
random.randrange(start,stop,step) สุ่มเลขมีช่วง
random.randint(min,max) สุ่มจำนวนเต็มมีช่วง
random.choice() สุ่มโดยหยิบจากค่า
random.shuffle() สลับข้อมูล
'''
for i in range(10):
    rand = random.randint(5,10)
    print(rand)