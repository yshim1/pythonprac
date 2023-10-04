#Property Decorator

"""
Recall that getters and setters are a useful took for achieving encapsulation (a way to prevent direct data modification)
Getters and setters involve defining a private attribute with a public means of accessing or modifying that attribute
"""

"""
The built-in property function accepts four optional arguments: fget, fset, fdel, and doc or docstring
The property function allows us to directly engage with the private attribute without a need to call the function name.
Instead, we can use regular operators such as (., =, and del)
"""
class Box:
  def __init__(self, weight):
    self.__weight = weight #Private variables

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
  
box = Box(10)

print(box.weight) #this calls .getWeight()

box.weight = 5 #this called .setWeight()

del box.weight #this calls .delWeight()

box.weight = -5 #box.__weight is unchanged 

#Using the property function allows us to interact with the weight attribute as if it were public instead of private


class Box:
 def __init__(self, weight):
   self.__weight = weight

 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight


 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight

 @weight.deleter
 def weight(self):
   del self.__weight
   
#Notice how methods  are renamed to weight, the getter is decorated with @property, weight is used as prefix for decorating the setter
#and deleter methods

#The first method must be a getter and is identified using the @property tag