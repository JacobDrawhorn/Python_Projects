class Vehicle:

    def __init__(self, horn):
        self.__horn = horn


class MyCar(Vehicle):

    def __init__(self, horn):
        self.__horn=horn

v1 = Vehicle('car')
v2 = MyCar('train')
print(v1.__dict__)
print(v2.__dict__)


