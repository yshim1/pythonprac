def add_five(num):
    print(num + 5)
    
print(add_five)     #output is <function add_five at 0x7fd7700e8040>. This is because function is an object
print(add_five(2))  #using parenthesis is how to invoke functions and execute code inside

# Decorating a function
def title_decorator(print_name_function):
    def wrapper():
        print('Sir:')
        print_name_function()
    return wrapper


def print_my_name():
    print('Yamlak')

decorated_function = title_decorator(print_my_name) #stores wrapper function into decorated_function
decorated_function() #Executes decorated function
print(decorated_function) #Notice how this print statement returns a function name with location
"""
passing print name function into title decorator function and defining a nested function (that adds functionality)
that will print sir and call print name function and return the calls made from wrapper
OUTPUT:
Sir
Yamlak
"""

#Decorator
@title_decorator #Must have same name as function
def print_yon_name():
    print('Yonathan')
    
print_yon_name()
"""
OUTPUT:
Sir
Yonathan
"""

#Decorators with parameters
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print('Sir:')
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_my_name(name, age, gender): #In order to accept arguments here in the title decorator, we have to allow args in wrapper and print_name_function
    print(name, f'you are {age} years old', f'you are a {gender}' )

print_my_name('Yamlak', 22, gender = 'Male')
