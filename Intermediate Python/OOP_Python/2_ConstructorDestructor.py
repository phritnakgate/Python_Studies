class Conc():
    def __init__(self,name,salary,department):
        self.name = name  
        self.salary = salary
        self.department = department
    def showData(self):
        print('ชื่อพนักงาน: {} \t'.format(self.name) +
              'เงินเดือน: {} \t'.format(self.salary) +
              'ตำแหน่งงาน: {}'.format(self.department))
    def __del__(self):
        print('Destructor')

obj1 = Conc('คนที่ 1',50000,'Accountant')
obj1.name = 'บอส'
obj1.showData()

print(isinstance(obj1,Conc))
print(isinstance(obj1,int))

print(dir(obj1))

print(obj1.__class__)