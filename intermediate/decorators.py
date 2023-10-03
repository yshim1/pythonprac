def add_five(num):
    print(num + 5)
    
print(add_five)     #output is <function add_five at 0x7fd7700e8040>. This is because function is an object
print(add_five(2))  #using parenthesis is how to invoke functions and execute code inside

#Decorating a function
def title_decorator(print_name_function):
    def wrapper():
        print('Shipoopie:')
        print_name_function()
    return wrapper


def print_my_name():
    print('Yamlak')

decorated_function = title_decorator(print_my_name)
print(decorated_function)


#Decorator
@title_decorator
def print_my_name():
    print('Yamlak')
print_my_name()

#Decorators with parameters
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print('Shipoopie:')
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_my_name():
    print('Yamlak')

print_my_name('Shimelis')