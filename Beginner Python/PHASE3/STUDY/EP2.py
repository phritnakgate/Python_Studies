#Python x txt file
import os
'''
open(<ชื่อไฟล์>,<mode>,<การเข้ารหัส(ไม่บังคับใส่)>)
mode ที่ใช้หลักๆจะมี 3 mode
r = Read only — เมื่อเปิดไฟล์ สามารถอ่านไฟล์ได้อย่างเดียว
w = Write — สามารถเปลี่ยนแปลงแก้ไขไฟล์นั้นได้(เขียนทับ) รวมถึงการสร้างและลบไฟล์ 
a = Append — เมื่อเปิดไฟล์ จะเพิ่มข้อมูลใหม่ต่อท้ายข้อมูลที่มีอยู่แล้วในไฟล์เดิม
'''
#1. การอ่านไฟล์ text
try:
    fr = open("P3_EP2txt.txt","r",encoding="utf-8")
    print(fr.read())
except FileNotFoundError:
    print("เช็คชื่อไฟล์ใหม่")

#2. การเขียนไฟล์ => write
try:
    fw = open("P3_EP2write.txt","w",encoding="utf-8")
    fw.write("eiei\n")
    fw.writelines("eueu") 
    fw.close()
    fw2 = open("P3_EP2write.txt","r",encoding="utf-8")
    line = fw2.readlines() #อ่านข้อมูล
    for x in line:
        print("=>",x)
except FileNotFoundError:
    print("เช็คชื่อไฟล์ใหม่")

#3. การเขียนไฟล์ => append
try:
    fa = open("P3_EP2append.txt","a",encoding="utf-8")
    for i in range(5):
        inp = input("ป้อนข้อความ: ")
        fa.writelines(inp+"\n")
    fa.close()
except FileNotFoundError:
    print("เช็คชื่อไฟล์ใหม่")

#4. ลบ text file
'''
import os ก่อนด้วยนะะะะะ
ลบ: os.remove("<ชื่อไฟล์>")
เช็คว่ามีมุ้ย: os.path.exists("<ชื่อไฟล์>")
''' 