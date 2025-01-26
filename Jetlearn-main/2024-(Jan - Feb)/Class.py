class Bird:
    def Intro(self):
        print("There are many types of birds")

    def Flight(self):
        print("Most of the birds can fly, but some cannot")

        return self
    
    Type = "Bird"

class Bird_Duck:
    def Intro(self):
        print("Ducks wade in water")

    def Flight(self):
        print("Some Ducks can fly")

    def Exclusive(self):
        return True

class Duck(Bird, Bird_Duck):
    pass

class Sparrow(Bird):
    def Flight(self):
        print("Sparrows can fly")

class Ostrich(Bird):
    def Flight(self):
        print("Ostriches cannot fly")

Duck1 = Duck()

print(Duck1.Exclusive())

print(Duck1.Type)


"""
Bird1 = Bird()

Sparrow1 = Sparrow()

Ostrich1 = Ostrich()

Ostrich1.Flight()
Sparrow1.Flight()
Bird1.Flight().Intro()
"""