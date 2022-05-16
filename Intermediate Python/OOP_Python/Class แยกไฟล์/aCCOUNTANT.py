from Employee import Employee
class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.age = age
    def _showData(self):
        super()._showData()
        print('อายุ: ' + str(self.age))