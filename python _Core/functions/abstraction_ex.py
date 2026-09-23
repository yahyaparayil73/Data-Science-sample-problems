
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    maths = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()

    def get_total(self):
        return self.maths + self.science + self.english

    def get_average(self):
        total = self.get_total()
        return total / 3

    def get_grade(self):
        average = self.get_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def get_result(self):
        average = self.get_average()

        if average >= 40:
            return "PASS"
        else:
            return "FAIL"