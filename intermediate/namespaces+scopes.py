#Built in namespace values, functions, and objects
print(dir(__builtins__))

x = 1
n = 'yamlak'

#prints the global objects/attributes
print(globals())

"""
Anytime we use the import statement to bring in a new module into our program, 
instead of adding every name from that module (such as all the names in the random module) 
to our current global namespace, Python will create a new namespace for it. This means 
there might be potentially multiple global namespaces in a single program. This will 
be masked away from us in the format seen with the random module (<module 'random' 
from '/usr/lib/python3.8/random.py'>).
"""

#local
def greet():
    greeting = 'hello'
    print(greeting)
    print(locals())
  
global_variable = 'global'

def add(num1, num2):
  nested_value = 'Inside Function'   
  print(num1 + num2)

add(5, 10) 
    
"""
We called locals() inside the add() function to get the local namespace generated 
when the function is executed. If we called locals() outside of a function 
in our program, it behaves the same as globals().

The value printed from calling locals() represents the namespace that 
only exists inside of the function. Notice even the function parameters
num1 and num2 exist alongside the variable name nested_value. The namespace 
does not include global_variable since it exists outside of the function (in the global namespace).
"""

#Enclosed Namespace
"""
We define a function called outer_function() and nest another function 
inside it called inner_function(). To generate a namespace, functions 
must be executed, so we are calling both of them.

Here, The outer_function() serves the role of an enclosing function while
inner_function is an enclosed function. By creating this structure, we 
generate an enclosing namespace - a namespace created by an enclosing 
function and any number of enclosed functions inside it.
"""

global_variable = 'global'
 
def outer_function():
  outer_value = "outer"
 
  def inner_function():
    inner_value = "inner"

    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    # Add locals() below
    print(locals())
    """
    <<{'outer_value': 'outer', 'inner_function': <function outer_function.<locals>.inner_function at 0x7f46b56bc820>}
    """
  inner_function()
 
outer_function()


def calc_paint_amount(width, height):
  square_feet = width * height
  def calc_gallons():
    return square_feet/400
  
  return calc_gallons()   #Why is there a return statement here? Because the outer function requires a return value otherwise it will return none when called

    

print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))



def enclosing_function():
  var = "value" #This is in the enclosing namespace

  def nested_function():
    nonlocal var  #Uncomment this line to change the value of var where the word after nonlocal is varname
    var = "new_value"           #Enclosed immutable variables cannot be modified within nested functions unless using the nonlocal kw

  nested_function()

  print(var)

enclosing_function()


#Global scope variables can be accessed but not modified
gravity = 9.8

def get_force(mass):
  global gravity  #Adding this line will allow us to modify the global variable gravity in our local scope. Can also be used to 
                        #declare + assign a global variable within the local scope
  gravity += 100
  return mass * gravity

print(get_force(60)) 
"""<<Program returns unboundlocalerror: local variable 'gravity' referenced before assignment"""


#LEGB RULE
"""
Scope Resolution: a search procedure for a name in the various namespaces
This rule shows the order in which the python will check namespaces to see if a name exists
Local -> Enclosing -> Global -> Built-in Scope
"""


age = 27 

def func(): 
  age = 42      

  def inner_func():
    print(age)  #Output will be 42 because python finds age exists as enclosed scope and terminates search
  
  inner_func() 

func()


"""
Scope defines which namespaces our program will look in to (to check names) and in what order. While multiple
namespaces usually exist at  once, this doe snot mean we can access all of them in different parts of our program

Namespaces is the mechanism for storing name-object pairs, while scope will serve as a rule system on where we
can retreive those names
"""

"""
Local Scope:

Calling a function will cause a local scope to be generated. Each subsequent function call will generate a new local scope
Local scope is the deepest level. Names in the local scope cannot be access or modified by any code called in outer scoeps
def favorite_color(): 
  color = 'Red'         color can only be accessed within the function definition
print(color) 
"""

#Enclosing/Nonlocal scope
def outer_function():
  enclosing_value = 'Enclosing Value'
 
  def nested_function():
    nested_value = 'Nested Value'
    print(enclosing_value)
  
  nested_function()

outer_function()
"""
In this example, the output of the print statement will be 'Enclosing Value'. This variable is able to be accessed
by the enclosed functions.
However, this can only be done going up, the deepest enclosed functions have access to items in the enclosing functions

ALSO: immutable objects or numbers can be accessed in enclosed function but cannot be modified
"""