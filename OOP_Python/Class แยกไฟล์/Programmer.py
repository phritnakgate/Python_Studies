from Employee import Employee
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