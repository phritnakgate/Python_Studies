#Inheritance
#class แม่
class Employee():
    #Class Variable
    _minsalary = 12000
    _maxsalary = 50000
    _companyname = 'Eiei Corp'

    def _getIncome(self):
        return self._salary * 12
    def __str__(self):
        return ('ชื่อพนักงาน = {} แผนก = {} เงินเดือน = {} รายได้ต่อปี = {}'.format(self.__name,self.__department,self.__salary,self._getIncome))

    def __init__(self,name,salary,department):
        #Instance Variable
        self.__name = name   #Protected Attribute
        self.__salary = salary
        self.__department = department
    def _showData(self):
        print('ชื่อพนักงาน: ' + self.getName() + '\n' +
              'เงินเดือน: ' + self.getSalary() + '\n'
            'ตำแหน่งงาน: ' + self.getDepartment())
    
    #setter method
    def setName(self,newname):
        self.__name = newname
    def setSalary(self,newsalary):
        self.__salary = newsalary
    def setDepartment(self,department):
        self.__department = department
    #Getter Method
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

#class ลูก
class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        
class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        
class Sale(Employee):
    __departmentName = 'แผนกขายสินค้า'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        
account = Accounting('eiei','12000')
print(account.__str__())
programmer = Programmer('buikem','50000')
sale = Sale('eueu','35000')