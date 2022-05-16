#หาผลรวมตัวเลข+ผลเฉลี่ย
func = int(input("เลือกประเภทอนุกรม 1=เลขคณิค 2=เรขาคณิต: "))
if func==1: #เลขคณิต
    a1 = float(input("ใส่ตัวเลขเริ่มต้น: "))
    d = float(input("ใส่ค่า d ของอนุกรมเลขคณิต: "))
    n = int(input("ใส่จำนวนพจน์: "))
    i = 1
    summation = 0
    if n > 1:
        while i <= n:
            summation+=a1 
            i+=1
            a1+=d 
        print(summation)
        av=summation/n
        print("ค่าเฉลี่ยคือ ", av)
    else:
        print("กรุณาใส่ n มากกว่า 1 และไม่เป็นทศนิยม")
elif func==2: #เรขาคณิต
    a1 = float(input("ใส่ตัวเลขเริ่มต้น: "))
    r = float(input("ใส่ค่า r ของอนุกรมเรขาคณิต: "))
    n = int(input("ใส่จำนวนพจน์: "))
    i = 1
    summation = 0
    if n>1:
        while i<=n:
            summation+=a1
            i+=1
            a1*=r
        print(summation)
        av=summation/n
        print("ค่าเฉลี่ยคือ ", av)
    else:
        print("กรุณาใส่ n มากกว่า 1 และไม่เป็นทศนิยม")
else:
    print("กรุณาใส่ค่าประเภทให้ถูกต้อง")