class Employee:

    def __init__(self):
        self.name = "Yahya"
        self._salary = 25000
        self.__password = "1234"


employee = Employee()

print(employee.name)

print(employee._salary)

print(employee.__password)  #causes error because it is protected using private(double underscore)