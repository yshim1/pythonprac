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

  @abstractmethod    #decorator. This makes sure AbstractEmployee cannot be instantiated
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