#Fibonacci Number
def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)
fibo = int(input("ใส่จำนวนพจน์ Fibonacci Number: "))
for i in range(fibo):
    print(fibonacci(i))