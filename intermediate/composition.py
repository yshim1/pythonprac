#Composition

class Component:
  
   # composite class constructor
    def __init__(self):
        print('Component class object created...')
  
    # composite class instance method
    def m1(self):
        print('Component class m1() method executed...')
  
  
class Composite:
  
    # composite class constructor
    def __init__(self):
  
        # creating object of component class
        self.obj1 = Component()
          
        print('Composite class object also created...')
  
     # composite class instance method
    def m2(self):
        
        print('Composite class m2() method executed...')
  
        # calling m1() method of component class
        self.obj1.m1()
  
  
# creating object of composite class
obj2 = Composite()
  
# calling m2() method of composite class
obj2.m2()

#Whenever we create an object of the composite class, we also create an object of the component class
#In composite method 2, we call we call m1() method of component class using instance var obj1 which has a refernece of the component class
#stored within itself
#Whenever m2() is called, component m1() will be called

"""
Inheritance is used where a class wants to derive the nature of parent class and then
modify or extend the functionality of it. Inheritance will extend the functionality
with extra features allows overriding of methods, but in the case of Composition, 
we can only use that class we can not modify or extend the functionality of it. 
It will not provide extra features. Thus, when one needs to use the class as it without 
any modification, the composition is recommended and when one needs to change the behavior 
of the method in another class, then inheritance is recommended.

Only use inheritance when you are sure the superclass will not be changed, otherwise go for composition
Typically, composition is favored
"""