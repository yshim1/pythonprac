#Interface
"""
The interface in object-oriented languages like python is a set of method signatures that the implementing class is 
expected to provide. Writing ordered code and achieving abstraction is possbile through interface implementation

Declaring Interface:
an interface is defined using python class statements and is a subclass of interface.Interface which is the parent class
for all interfaces

ATTENTION
There are no interfaces on a language level meaning library implementations do exist such as

abc, typing.protocols, zope, custom implementations via metaclasses
"""

# import zope.interface
    
    
# class MyInterface(zope.interface.Interface):
#     x = zope.interface.Attribute("foo")
#     def method1(self, x):
#         pass
#     def method2(self):
#         pass
    
# @zope.interface.implementer(MyInterface)
# class MyClass:
#     def method1(self, x):
#         return x**2
#     def method2(self):
#         return "foo"
      
# obj1 = MyClass()
  
# print(obj1.method1(5))
# print(obj1.method2())

from typing import Protocol
 
class Animal(Protocol):
   def eat(self, food) -> float:
       ...
 
   def sleep(self, hours) -> float:
       ...
       
"""
A protocol is a formalization of Python's duck typing ideology. Protocols allow for structural subtyping which is checking
whether two classes are compatible based on available attributes and functions alone

Python is dynamically typed meaning data types (int, bool, float, str) are inferred at runtime and not declared like java
Dynamic typing is also called duck typing: "if it walks like a duck and quaks like a duck, then it must be a duck".

Simiarly,
if the objects has the same attributes/functions, they should be treated similarly and can be passed to functions
requiring the other type.
"""