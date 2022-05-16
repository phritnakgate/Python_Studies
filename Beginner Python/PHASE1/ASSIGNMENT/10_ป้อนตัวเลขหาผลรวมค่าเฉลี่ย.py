#ป้อนตัวเลขหาผลรวมค่าเฉลี่ย
start = 1
stop = int(input("ป้อนจำนวนตัวเลข: "))
summation = 0
while(start <= stop):
    number = int(input("ป้อนตัวเลข: "))
    start+=1
    summation+=number
print(summation)
av = summation / stop
print("ค่าเฉลี่ย คือ ", av)