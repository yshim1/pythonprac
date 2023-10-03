#Property Decorator
class Box:
  def __init__(self, weight):
    self.__weight = weight

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

