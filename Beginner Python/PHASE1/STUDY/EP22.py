#Loop ซ้อน Loop
'''
i = 1
while i <= 3:
    j=1
    while j<= 5:
        print("รอบที่ = ", i, "ตำแหน่งที่ = ", j)
        j+=1
    i+=1
'''
for a in range(1,4):
    print("รอบที่ = ", a)
    for b in range(1,6):
        print("รอบที่ = ", b)