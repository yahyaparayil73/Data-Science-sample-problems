# class hikma:

#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print('The employee details is given below :')
#         print(f'The Employee name is {self.name}')
#         print(f'Monthly salary is {self.salary}')
#         print(f'Annual Salary is {self.salary*12}')

#     def salary_increment(self):
#             print(f'The present salary is {self.salary}')
#             new_salary = int(self.salary + self.salary*0.3)
#             print(f'New incremented Salary is {new_salary}')

# employee = hikma('Yahya',25000)

# # employee.display()
# employee.salary_increment()



#the same program without oop is given below: 

def display(name,age):
    print(f'The employee name is {name}  and age is {age}')
  


print('***************** Employee Details Tracker : *****************')

name = input('Enter the employee name :')
age = int (input ('Enter the Age :'))

display(name,age)





