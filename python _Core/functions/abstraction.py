from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Wild_Animals(Animal):
    def make_sound(self,name):
        print(f'{name} Roars')

Lion = Wild_Animals()
Lion.make_sound('Yahya')

