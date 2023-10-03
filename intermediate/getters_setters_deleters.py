"""
Using getter, setter, and deleter functions are one 
way to implement encapsulation within Python where 
the state of class attributes can be handled within the class
"""
class Animal:
  def __init__(self, name):
    self._name = name
    self._age = None       #Single underscore means only to be used within module

  def get_age(self):
    return self._age

  def set_age(self, new_age):
    if isinstance(new_age, int):
      self._age = new_age
    else:
      raise TypeError

  def delete_age(self):
    print("_age Deleted")
    del self._age