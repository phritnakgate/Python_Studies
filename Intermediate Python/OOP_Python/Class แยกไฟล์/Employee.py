class Employee:
    __minSalary = 12000
    __maxSalary = 50000
    companyName = 'บริษัท อุอิ คุคิ จำกัด'
    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self._department = department
    def _showData(self):
        print('ชื่อพนักงาน: ' + self.getName() + '\n' +
              'เงินเดือน: ' + self.getSalary())
    def getName(self):
        return self._name
    def getSalary(self):
        return str(self._salary)