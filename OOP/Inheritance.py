 #Inheritance
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

# Write your code below
class Admin(Employee):          #Admin class inherits from Employee parent class
  pass

  #def say_id(self):            This will override parent say_id()
    #print('I am an admin')
    #super().say_id()           This will call parent class say_id()
e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

#super()
"""
Super is a proxy object. With this proxy object we can invoke the method of an object's parent class(also called superclass)
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

# Write your code below
class Manager(Admin):
  def say_id(self):
    print('I am in charge')
    super().say_id()
e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()


#Multiple inheritance
"""
There are 2 ways to invoke multiple inheritance. One is to make a class that directly inherits 2 classes. The other way is to 
have a class inherit from a superclass that also inherits from another superclass (super-superclass)
"""
class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))

class Cat(Animal):
  pass

class Angry_Cat(Cat):
  pass

my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() # Mr. Cranky says, Hi!



class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):    #The super() function calls on employee.__init__() because employee is the first parameter
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, 'Admin') #When calling user function, you need to pass self. 
                                          #This is to make sure the admin instance is passed through the user function
    

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()

"""
Inheritance allow us to define a class that inherits all the methods and properties from another class. 
The parent class is called the base class and the child class is called the derived class. 
"""

"""
Python also supports multiple inheritance where one class can inherit from anu number of other classes. This allows us to 
describe complex relationships between objects with minimal repeated code
"""