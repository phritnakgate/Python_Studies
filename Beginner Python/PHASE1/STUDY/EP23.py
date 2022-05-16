#break/continue => break หยุดการทำงาน continue ข้ามการทำงาน
'''
i = 1
while i<=10:
    print("รอบที่ = ", i)
    if i == 5:
        break
    i+=1
else:
    print("จบโปรแกรม")
'''
i = 0
while i <= 10:
    i+=1
    if(i%2 ==0):
        continue
    else:
        pass
    print("รอบที่ = ", i)