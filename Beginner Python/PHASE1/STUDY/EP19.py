"""
เจาะลึก String #2
6. การต่อ string
"""
fname="phrit"
lname="nakgate"
age="18"
full = fname+lname+age
print(full)

"""7.จัดรูปแบบการแสดงผล"""
text="{} {} อายุ {} ปี "
print(text.format(fname,lname,age))

"""8.นับจำนวนคำในประโยค"""
market = "mango stickyricewithmango at gourmet market"
print(market.count("mango"))

"""9.เช็คคำขึ้นต้น/ลงท้าย"""
lottery = "574028"
if lottery.startswith("5") and lottery.endswith("8"):
    print("เย่")
else:
    print("ไม่เย่")