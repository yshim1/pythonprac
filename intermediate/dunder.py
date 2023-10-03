# For an int and an int, + returns an int
2 + 4 == 6

# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]


class Animal:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

  def __add__(self, another_animal):
    return Animal(self.name + another_animal.name)

a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2 #The line of code a3 = a1 + a2 invokes the .__add__() 
             #method of the left operand, a1, with the right operand a2 
             #passed as an argument. The name attributes of a1 and a2 
             #are concatenated using the .__add__() parameters, self and 
             #another_animal. The resulting string is used as the name of 
             #a new Animal object which is returned to become the value of a3.
print(a1) # Prints "Horse"
print(a2) # Prints "Penguin"
print(a3) # Prints "HorsePenguin"

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)     #Override + operator

  # Write your code
  def __len__(self):
    return len(self.attendees)          #Override len() function
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

