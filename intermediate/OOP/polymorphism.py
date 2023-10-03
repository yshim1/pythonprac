#Polymorphism
"""
In computer programming, polymorphism is the ability to 
apply an identical operation onto different types of objects. 
This can be useful when an object type may not be known at the
program runtime. Polymorphism can be applied using Python in multiple ways.

Polymorphism ssentially means a subclass can override a method of the base class. Somewhat similar to ducktyping, however,
in ducktyping the method name is the same but the function is different depending on the class and there is no inheritance involved.
"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
meeting = [Employee(), Admin(), Manager()]
for item in meeting:
  item.say_id()