print('Enter the student details:')
print()
name = input('Enter the name of student :')
id = int(input('Enter the student ID : '))
physics_mark = int(input('Enter marks obtained for physics : '))
maths_mark = int(input('Enter marks obtained for Maths : '))
chemisty_mark = int(input('Enter marks obtained for Chemsistry : '))
biology_mark = int(input('Enter marks obtained for Biology : '))
computer_mark = int(input('Enter marks obtained for Computer : '))


class Student_marks:

    def __init__(self,name,id,physics_mark,maths_mark,chemisty_mark,biology_mark,computer_mark):
        self.name = name
        self.id = id
        self.physics_mark = physics_mark
        self.maths_mark = maths_mark
        self.chemisty_mark = chemisty_mark
        self.biology_mark = biology_mark
        self.computer_mark = computer_mark

    def get_total_marks(self,physics_mark,maths_mark,chemisty_mark,biology_mark,computer_mark):
        sum = self.physics_mark + self.maths_mark + self.chemisty_mark + self.biology_mark + self.computer_mark 
        print(f'The total marks = {sum}')

    # def get_total_percentage(self):

