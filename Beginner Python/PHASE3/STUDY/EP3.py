#Main
'''
เรียกใช้งาน module โดย custom ชื่อ 
    import <Module> as <ชื่อที่ต้องการเรียกในโค้ด>
เรียกใช้งานเฉพาะ function
    from <Module> import <function>
Package => folder เก็บ module ต่างๆ
    import <Package>.<Module>
    from <Package>.<Module> import <function>
'''
import MODULE.EP3_Module as addsub
from MODULE.EP3_Module2 import city
addsub.addition(5,10,20)
addsub.substract(32,22)
print(addsub.pii)
print(addsub.rt2)
print(city["Songklha"])