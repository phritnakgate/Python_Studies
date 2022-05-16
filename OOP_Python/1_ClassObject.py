#การสร้าง class
class Employee:
    #สร้าง method
    def detail(self,name,salary):
        self.name = name
        self.salary = salary
    def showData(self):
        print('ชื่อพนักงาน: {} \t'.format(self.name) +
              'เงินเดือน: {}'.format(self.salary))

#การสร้าง object
obj1 = Employee()
obj1.detail('คนที่ 1', 50000)
obj1.showData()

obj2 = Employee()
obj2.detail('คนที่ 2', 50000)
obj2.showData()

obj3 = Employee()
obj3.detail('คนที่ 3', 50000)
obj3.showData()