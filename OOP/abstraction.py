from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name):
    self.name = name

  @abstractmethod
  def make_noise(self):
    pass

class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))

class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))

kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"

from abc import ABC, abstractmethod

class AbstractEmployee(ABC):    #Abstract employee inherits from Abstract Base Class. This means it cannot be instantiated
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod    #decorator. This makes sure AbstractEmployee cannot be instantiated. Has declaration but not implementation
  def say_id(self):
    pass

# Write your code below
class Employee(AbstractEmployee):
  def say_id(self):
    print('My ID is {}'.format(self.id))


e1 = Employee()
e1.say_id()
#an abstract employee
#abc_employee = AbstractEmployee(ABC) <<TypeError: Can't instantiate abstract class Abstract Employee with abstract method say_id

#Abstraction defines what an abstract employee is but not the creation of one

"""
A class that has a metaclass derived from ABCMETA cannot be instantiated unless all of its abstract methods and properties are overriden

"""

#What is abstraction used for?
"""
Helps with the design of code by defining necessary behaviors to be implemented within a class structure. In doing so,
abstraction helps avoid leaving out or ovrelapping class functionality as class hierarchies get larger.

Two steps to making an abstract class that cannot be instantiated:
1. Inheriting from ABC or Abstract Base Class
2. Defining this class that inherits from ABC with abstractmethod decorators

For example:
The make noise method is inherited by all animals that inherit from the animal class since all animals make a noise. However each animal
makes different noises thus needing overriding. Each subclass of Animal is required to define their own make oise method or an error will
occur

Summarize:
Abstraction supports the design of an organized class structure.
"""

"""
ABC also supports implicit interfaces through the concept of virtual subclasses but you have to call register for every 
implementation
"""
class Giraffe:  # no base class needed!
   def eat(self, food) -> float:
       return 0.

class Animal(ABC):
    ...

Animal.register(Giraffe)  # achieves the same as implicit Protocol