#Encapsulation
"""
The process of making methods and data hidden inside the object they relate to
This is done by access modifiers like public, protected, private
"""

#Public: Can be accessed from anywhere
#Protected: can be accessed from code within the same module
#Private: can only be accessed from code within the class that these members are defined

#self._x << The underscore signifies protected. Accessing protected member outside of module will not cause an error
#it is added by developers to inform other developers that they should be careful when accessing this member in such a manner

#self.__x <<Double underscore means private. Name mangling. Members that are preceded with 2 underscores
#have their names modiefied in the background to obj._Classname__x. While they can still be accessed, 
#the purpose of this mechanism is to prevent clashing member names of any inheriting classes that might define a member of the
#same name. Dunder method names are not mangled

class Employee():
    def __init__(self):
        self.id = None
        # Write your code below
        self._id = None
        self.__id = None #Name wrangling returns _Employee__id when dir(e) is called

e = Employee()
print(dir(e))