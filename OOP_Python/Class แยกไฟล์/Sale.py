from Employee import Employee
class Sale(Employee):
    __departmentName = 'แผนกขายสินค้า'
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.area = area
    def _showData(self):
        super()._showData()
        print('พื้นที่ทำงาน: ' + self.area)