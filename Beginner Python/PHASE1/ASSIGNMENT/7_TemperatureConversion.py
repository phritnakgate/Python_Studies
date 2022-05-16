#โปรแกรมเปลี่ยนอุณหภูมิ
temp = input("ใส่อุณหภูมิ เช่น 25c กำหนดให้ c=celcius f=farenheit k=kelvin : ")
unit = temp[-1]
unit = unit.lower()
num = float(temp[:-1])
if unit == "c":
    f=((num/5)*9)+32
    k=num+273
    out="อุณหภูมิ {:.2f} C = {:.2f} F = {:.2f} K"
    print(out.format(num, f, k))
elif unit == "f":
    c=((num-32)/9)*5
    k=c+273
    out="อุณหภูมิ {:.2f} F = {:.2f} C = {:.2f} K"
    print(out.format(num, c, k))
elif unit == "k":
    c=num-273
    f=(((num-273)/5)*9)+32
    out="อุณหภูมิ {:.2f} K = {:.2f} C = {:.2f} F"
    print(out.format(num, c, f))
else:
    print("ใส่ค่าใหม่")