#Polymorphism

#class แม่
class Employee():
    _minsalary = 12000
    _maxsalary = 50000
    _companyname = 'Eiei Corp'
    def __init__(self,name,salary,department):
        self._name = name  
        self._salary = salary
        self._department = department
    def _showData(self):
        print('ชื่อพนักงาน: ' + self.getName() + '\n' +
              'เงินเดือน: ' + self.getSalary())
    def getName(self):
        return self._name
    def getSalary(self):
        return str(self._salary)
#class ลูก
class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.age = age
    def _showData(self):
        super()._showData()
        print('อายุ: ' + str(self.age))
        
class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self,name,salary,exp,skill):
        super().__init__(name,salary,self.__departmentName)
        self.exp = exp
        self.skill = skill
    def _showData(self):
        super()._showData()
        print('ประสบการณ์: ' + self.exp() + '\n' +
              'ทักษะ: ' + self.skill())
class Sale(Employee):
    __departmentName = 'แผนกขายสินค้า'
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.area = area
    def _showData(self):
        super()._showData()
        print('พื้นที่ทำงาน: ' + self.area)
            
account = Accounting('Kong',40000,30)
account._showData()
dev = Programmer('Buikem',20000,'0 year','Python')
dev._showData()
sale = Sale('Nutto',35000,'CNX')
sale._showData()