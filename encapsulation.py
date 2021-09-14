# create a parent class conaining a private function and a child class containing a private function

class Vehicle:

    def __init__(self, horn):
        self.__horn = horn


class MyCar(Vehicle):

    def __init__(self, horn):
        self.__horn=horn

# creates variables to put in classes and prints the functions

_v1 = Vehicle('car')
_v2 = MyCar('train')
print(_v1.__dict__)
print(_v2.__dict__)


