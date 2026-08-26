class hikma:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print('The employee details is given below :')
        print(f'The Employee name is {self.name}')
        print(f'Monthly salary is {self.salary}')
        print(f'Annual Salary is {self.salary*12}')

    def salary_increment(self):
            print(f'The present salary is {self.salary}')
            new_salary = int(self.salary + self.salary*0.3)
            print(f'New incremented Salary is {new_salary}')

employee = hikma('Yahya',25000)

# employee.display()
employee.salary_increment()
    