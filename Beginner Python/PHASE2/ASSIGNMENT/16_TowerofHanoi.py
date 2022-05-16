#หอคอยฮานอย
'''
n = จำนวนจาน
A = เสา1
B = เสา2
C = เสา3
สมมุติมีจาน n ใบ ให้จานบนสุดเป็นจานใบที่ 1 และถัดมาเป็นใบที่ 2 และล่างสุดเป็นใบที่ n
และให้หลักทั้ง 3 ชื่อ A B C ไล่จากซ้ายไปขวา
หลักการคือ
- จานใบที่ 1 จะขยับทุก 2 ตา ใบที่ 2 ขยับทุก 2^2 = 4 ตา ใบที่ 3 ขยับทุก 2^3 = 8 ตา ใบที่ n ขยับทุก 2^n ตา
- ทิศทางการย้ายของแต่ละจานต้องมีความตายตัว คือ A -> B -> C -> A หรือ A -> C -> B -> A ตลอดเกม โดยจานที่ 1, 3, 5,... จะมีทิศทางเหมือนกัน ส่วน 2, 4, 6,... จะเป็นทิศตรงกันข้าม
- ใบที่ n จะขยับครั้งเดียวเท่านั้น และเป็นการขยับตอนกลางเกม และใบที่ n-1 จะขยับแค่ 2 ครั้ง ใบที่ n-2 ขยับ 2^2 = 4 ครั้ง ใบที่ 1 ขยับ 2^(n-1) ครั้ง
- จำนวนครั้งที่ขยับรวมทั้งหมดคือ (2^n)-1 ครั้ง
'''
t = 0 # ตั้งจำนวนตาเริ่มต้น
def hanoi(n,a,b,c): # นิยามฟังก์ชันฮานอย พารามิเตอร์คือจำนวนจาน ตามด้วยชื่อหลักทั้งสาม
    global t
    if(n>0): # จะมีการกระทำเกิดขึ้นตราบใดที่ n มากกว่า 0
        hanoi(n-1,a,c,b) # เรียกใช้ฟังก์ชันเดิมที่ n น้อยกว่าอยู่ 1 โดยสลับ b กับ c
        t += 1 # นับบวกจำนวนตา
        print('%d. ย้ายจานที่ %d จาก %s ไป %s'%(t,n,a,b)) # แสดงวิธีการย้าย
        hanoi(n-1,c,b,a) # เรียกใช้ฟังก์ชันเดิมที่ n น้อยกว่าอยู่ 1 โดยสลับ a กับ c
hanoi(3,'A','B','C') # เรียกใช้ฟังก์ชันเพื่อเล่นเกมที่มี 3 จาน