# oop is design pattern that allows us to create objects that have properties and methods. It is a way to organize code and make it more reusable.
# and it keeps your code DRY (Don't Repeat Yourself)
# class in oop is a blueprint for creating objects. It defines the properties and methods that the objects will have.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person1=Person("Alice",30)
print(person1.greet())
#  person2=Person() this will raise an error b/c the __init__method requires two arguments.which are name and age.

# with out __init__ method we have to set the properties of the object manually which is not efficient and can lead to errors. with __init__ method we can set the properties of the object when we create it.

# static /class variables are shared among all instances of the class. they are defined outside of the __init__ method and are accessed using the class name.
# instance variables are unique to each instance of the class. they are defined inside the __init__ method and are accessed using the self keyword.
class Student:
    school_name="Addis ababa university"
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        self.geneder="custom"
student1=Student("Bob",20)
student2=Student("Charlie",22)
print(student1.school_name) # this will print "Addis ababa university"
print(student2.school_name) # this will also print "Addis ababa university"
Student.school_name="Addis ababa university of technology" # this will change value of the static variable for all instances of the class.
print(student1.school_name) 
# self parameter is a referenc to the current instance of the class.and it has to be the first parameter of any method in the class.
# why self b/c python dont know which object's properties do you want to access or modify. so we use self to specify that we want to access or modify the properties of the current instance of the class.
# and it can be named anything whatever you want but by convention we use self. and it is not a keyword in python, it is just a convention.
