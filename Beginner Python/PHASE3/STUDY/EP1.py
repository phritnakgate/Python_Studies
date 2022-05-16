#Exception => เหตุการณ์ที่ทำให้เกิดข้อผิดพลาด ทำยังไงให้โปรแกรมจัดการข้อผิดพลาดนั้นได้
'''
ระหว่างการทำงานโปรแกรม เกิดข้อผิดพลาดขึ้นทำให้โปรแกรมหยุดทำงาน
เช่น เขียน upload รูปภาพ แต่ user upload video เราต้องเขียนให้โปรแกรมแก้ปัญหานี้เพื่อให้ส่วนอื่นทำงานต่อ
'''
#แก้ปัญหาโดยใช้ try...except
"""
try:
    คำสั่งปกติ
except:
    คำสั่งเมื่อเกิดข้อผิดพลาด
"""
try:
    a=float(input("กรุณากรอกเลขแรก: "))
    b=float(input("กรุณากรอกเลขหลัง: "))
    result = a/b    
    print(result)
except ValueError:              #ถ้าเราใส่ except เฉยๆ เราจะไม่รู้ข้อผิดพลาด
    print("ป้อนตัวเลข only naja")
except ZeroDivisionError:
    print("มันหารด้วย 0 บ่ดั้ยนะ")
except TypeError:
    print("ชนิดข้อมูลไม่ตรงกันบ่าววว")
finally:    #finally => มีหรือไม่มีข้อผิดพลาดก็รันต่อได้ภายใต้ finally
    print("ทำงานต่อปาย...")
#else กับ try...except => ถ้า try ผ่านทำ else ต่อ แต่ถ้ามีข้อผิดพลาดก็ไม่รันต่อ
'''
else:       
    print("จบโปรแกรม")
'''

#การลดรูป exception/จำชื่อ error ไม่ด้าย
'''
except Exception as <ตัวแปร>:
    print(<ตัวแปร>) 
'''

#try-except-finally ทำงานกับ while
while True:
    try:
        print("จบการทำงานพิมพ์ 0 คู่")
        name = input("USERNAME: ")
        c=float(input("กรุณากรอกเลขแรก: "))
        d=float(input("กรุณากรอกเลขหลัง: "))
        if c==0 and d==0:
            break
        if name == "boss":
            raise Exception("มี user นี้ในระบบแล้วววว")
        else:
            result2 = c+d
            print(result2)
    except Exception as err:
        print("ข้อผิดพลาด คือ ",err)
    finally:
        print("ทำงานต่อปาย...")