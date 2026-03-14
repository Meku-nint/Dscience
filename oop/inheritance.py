# inheritance is a fundamental concept in oop that allows a child class to inherit properties and methods from a parent class.
# to create a child class pass the parent class as an argument when defining the child class. the child class can then override or extend the properties and methods of the parent class.
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        return "Some sound"
class Dog (Animal):
    def __init__(self,name,breed):
        super().__init__(name,"Dog") # this will call the __init__ method of the parent class and set the name and species properties of the dog object.
        self.breed=breed
    def make_sound(self):
        return "Woof!"
dog1=Dog("Buddy","Golden Retriever")
print(dog1.name) # this will print "Buddy"