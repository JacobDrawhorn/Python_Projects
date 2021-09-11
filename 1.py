
# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\n Arms: {}\n DNA: {}\n Origin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# child class of instance
class Human(Organism):
    name = "Jacob"
    species = "Homosapian"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\nDestroy the Earth!"
        return msg

# another child class instance
class Dog(Organism):
    name = "Cocoa"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nDog bites intruder!"
        return msg
        




if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())
    

