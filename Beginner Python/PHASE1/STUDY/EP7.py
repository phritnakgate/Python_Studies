#รับข้อมูลจาก keyboard => input()
fname = str(input("Please input your first name: "))
lname = str(input("Please input your last name: "))
age=int(input("Please input your age: "))
fage=age + 10
fage = str(fage)
print("Your name is: "+fname +"\t" +lname)
print("Your 10 year future age is: " +fage)