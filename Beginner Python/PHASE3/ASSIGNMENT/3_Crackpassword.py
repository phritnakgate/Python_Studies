#Crack PWD
import random
ATM_PASSWORD="934"
result=""               #สำหรับเก็บผลลัพธ์
while result != ATM_PASSWORD:
    result=""
    for letter in range(len(ATM_PASSWORD)):
        list_number = random.choice("0123456789")
        result="".join(list_number)+str(result)
        print("SEARCH= ",result)
print("CRACKED COMPLETE PIN IS: ",result)