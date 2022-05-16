
'''
Public Method
    def __init__(self,name,salary,department):
        #Public Attribute
        self.name = name  
        self.salary = salary
        self.department = department
    def showData(self):
        print('ชื่อพนักงาน: {} \t'.format(self.name) +
            'เงินเดือน: {} \t'.format(self.salary) +
            'ตำแหน่งงาน: {}'.format(self.department))
'''
'''
#Protected => ใส่ underscore ด้านหน้าตัวแปร
    def __init__(self,name,salary,department):
        #Protected Attribute
        self._name = name  
        self._salary = salary
        self._department = department
    def _showData(self):
        print('ชื่อพนักงาน: {} \t'.format(self._name) +
            'เงินเดือน: {} \t'.format(self._salary) +
            'ตำแหน่งงาน: {}'.format(self._department))
obj1 = Employee('Boss',22000,'Computer Engineering')
obj1._name = 'Buikem'
obj1._showData()
'''
#Private => underscore 2 ตัว
class Employee():
    #Class Variable
    _minsalary = 12000
    _maxsalary = 50000
    _companyname = 'Eiei Corp'

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

obj1 = Employee('Boss','22000','Computer Engineering')
obj1._showData()
print(Employee._companyname)
print('เงินเดือนต่ำสุดของพนักงาน คือ '+str(Employee._minsalary))