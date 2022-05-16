#ตัวเลขขั้นบันได
'''
Example
input: 3
output: 1
        12
        123
'''
last = int(input("ป้อนเลขท้าย: "))
for row in range(1,last+1):
    for column in range(1,row+1):
        print(column, end='')
    print(" ")