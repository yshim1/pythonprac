#Syntax Errors
"""
Caught during special parsing stage before a program is executed. Prevent entire program from running
"""

#Exceptions are runtime errors, occur during program execution i.e. NameError
#Exceptions and syntax make up 2 core categories for any error we will run into

#A traceback is a tool to gain insight into exception. Summary includes exception type, message, series of function calls
#that precede the exception, file names, and line numbers


#Built-in exceptions
#Exceptions are also objects. Most inherit from a class called exception; however, they are all derived directly or
#indirectly from the BaseException class. We can examine base classes by using the __bases__ attribute on any exception

print(NameError.__bases__) #<<Out put is (<class 'Exception'>,)
print(Exception.__bases__) #<<Out put is (<class 'BaseException'>,)

#Full hierarchy of exceptions
"""
BaseException
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
"""

#Raising Exceptions
"""
Raise keyword allows for us to throw an exception at any time. This lets us stop our program execution immediately and provide
a useful error message
"""

raise NameError     #We can either raise an exception by class name. This calles the constructor with no argument
#or 
raise NameError('Custom Message')   #or by class constructor

def open_register(employee_status):
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    # Alternatives: raise TypeError() or TypeError('Message')
    raise TypeError

def open_register(employee_status):
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    raise Exception('Employee does not have access!')

#Exception handling
"""
Exception handling: programs continue executing even after encountering an exception. It is accomplished by using try/except
Python will attempt to execute try block, if no exception is encountered, except clause is skipped. If exception is encountered in try
block then python will immediately stop executing code and begin code inside except block (handler)
"""
colors = {
    'red': '#FF0000',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
}

for color in ('red', 'green', 'yellow'):
  try:
    print('The hex value of ' + color + ' is ' + colors[color])
  except:
    print('An exception occurred! Color does not exist.')
  print('Loop continues...')
  
staff = {
  'Austin': {
      'floor managers': 1,
      'sales associates': 5
  },
  'Melbourne': {
      'floor managers': 0,
      'sales associates': 8
  },
  'Beijing': {
      'floor managers': 2,
      'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  # Write your code below:
  try:
    print_staff_report(location, staff)
  except:
    print('Could not print sales report for ' + location)

#Catching specific exceptions
"""
It is generally considered best practice to be as specific a possible with exceptions we
want to raise unless there's a reason for catching any type of exception
"""
try:
    print(undefined_var)
except NameError:
    print('We hit a NameError')
#The except block only checks for name errors

try:
    print(undefined_var)
except NameError as errorObject:
    print('We hit a NameError')
    print(errorObject)
#As keyword allows us to capture as exception object. This object hosts info about specific error that occured
staff = {
  'Austin': {
    'floor managers': 1,
    'sales associates': 5
  },
  'Melbourne': {
    'floor managers': 0,
    'sales associates': 8
  },
  'Beijing': {
    'floor managers': 2,
    'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  try:
      print_staff_report(location, staff)
  # Write your code below:
  except ZeroDivisionError as e:
      print('Could not print sales report for ' + location)
      print(e)

#Handling Multiple Exceptions
"""
We can list more than one exception type in a tuple with a single except clause
"""
try:
    pass
except (NameError, ZeroDivisionError) as e:
    print('We hit an Exception!')
    print(e)

#It is also possible to use multiple except clauses within a single try clause
try:
    # Some code to try!
    pass
except NameError:
    print('We hit a NameError Exception!')
except KeyError:
    print('We hit a TypeError Exception!')
except Exception:
    print('We hit an exception that is not a NameError or TypeError!')
    
#If the exception is not listed in the tuple, then any other exception will be handled by the third clause
#Python executes the first one that matches its type. Last clause is generally used as a generic exception
#as back up if no other specific exception gets caught


#else clause
"""
Only executed if no exception was encountered in the try clause
"""
try:
  check_password()
except ValueError:
  print('Wrong Password! Try again!')
else:
  login_user()
  # 20 other lines of imaginary code

#Why use else clause? Why not just put all our code in the try block
"""
The use of the else clause is better than adding additional code to the try
clause because it avoids accidentally catching an exception that wasn’t 
raised by the code being protected by the try … except statement.
"""

"""
This suggestion is valid in this case since in the alternative style, the 
ValueError could occur in any of the other lines of code other than check_password(),
and it would be challenging to tell where it came from.
"""

customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  # Write your code below:
  try:
    rewards_number = customer_rewards[customer]
  except KeyError:
    print('Customer was not found in rewards program!')
  else:
    print('Rewards account number is: ' + str(rewards_number))


customer = 'Mario'
display_rewards_account(customer)

#Finally Clause
"""
This clause executes regardless of exception being found or not
"""
try:
  check_password()
except ValueError:
  print('Wrong Password! Try again!')
else:
  login_user()
  # 20 other lines of imaginary code
finally:
  load_footer()
  
"""
Finally can be used independently (without except or else clause)
"""
try:
    check_password()
finally:
    load_footer()
    # Other code we always want to run
import database

instrument = 'Kora'
database.connect_to_database()

try:
  database.display_instrument_info(instrument)
except KeyError:
  print('Oh no! This instrument does not exist.')
else:
  print(instrument)
# Write your code below: 
finally:
  database.disconnect_from_database()


#User-defined exceptions
class CustomError(Exception):
    pass

class LocationTooFarError(Exception):
   pass

def schedule_delivery(distance_from_store):
    if distance_from_store > 10:
        raise LocationTooFarError
    else:
        print('Scheduling the delivery...')
        
inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}


#Write your code below (Checkpoint 2):
class InventoryError(Exception):
  pass


def submit_order(instrument, quantity):
  supply = inventory[instrument]
  if quantity > supply:
    raise InventoryError
  else:
  # Write your code below (Checkpoint 3 & 4): 
    inventory[instrument] -= quantity
  
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)

#Customizing User-defined Exceptions
class LocationTooFarError(Exception):
   def __init__(self, distance):
       self.distance = distance
       
   def __str__(self):
        return 'Location is not within 10 km: ' + str(self.distance)

# Write your code below (Checkpoint 1 & 2)
class InventoryError(Exception):
  def __init__(self, supply):
    self.supply = supply
  
  def __str__(self):
    return 'Available supply is only ' +str(self.supply)

inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  # Write your code below (Checkpoint 3)
  if quantity > supply:
    raise InventoryError(supply)
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)

#User-defined exceptions
class LocationTooFarError(Exception):
   def __init__(self, distance): #takes distance as parameter b/c it is needed in str method that returns message when exception is hit
       self.distance = distance
       
   def __str__(self):
        return 'Location is not within 10 km: ' + str(self.distance)
