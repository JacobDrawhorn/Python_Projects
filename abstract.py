
# import ABC 
from abc import ABC, abstractmethod

# create parent class

class AbstractClass(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def eat(self):
        pass

# create child class

class Parents(AbstractClass):
    def eat(self):
        return "eat solid food "+ str(self.value) + " times each day"

class Babies(AbstractClass):
    def eat(self):
        return "Milk only "+ str(self.value) + " times or more each day"

# call classes and print

food = 3    
mom = Parents(food)
print("moms ----------")
print(mom.eat())

infant = Babies(food)
print("infants ----------")
print(infant.eat())
