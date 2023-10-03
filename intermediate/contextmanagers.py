with open("file_name.txt", "w") as file:
   file.write("How you gonna win when you ain't right within?")
"""
With statement is the most common and pythonic way of invoking context managers in python. 

The with statement calls the built-in open() function on 'file_name.txt' with a mode of 'w' which represents write mode

The as clause assigns object opened to a target variable called filed

file.write() writes a sentence to 'file_name.txt'
"""

#Code without a with statement
file = open("file_name.txt", "w") #Manually open
try:
   file.write("How you gonna win when you ain't right within?")
finally:
   file.close() #Manually close

"""
By using a with statement, it serves as a context manager where files are automatically closed after script completion
"""
try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()
with open('file_name.txt', 'r') as open_file:
  print(open_file.read())
  
try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()


with open('file_name.txt', 'r') as open_file:
  print(open_file.read())


#Class based context managers
#__enter__ method: Allows for setup of context managers. Begins runtime context

#__exit__ method: ensures breakdown of context manager. takes care of closing open resources no longer in use

class ContextManager:
  def __init__(self):
    print('Initializing class...')
 
  def __enter__(self):
    print('Entering context...')
 
  def __exit__(self, *exc):
    print('Exiting context...')
"""
By implementing the 2 methods, we are implementing the context management protocol
"""
with ContextManager() as cm:
  print('Code inside with statement')
"""
Output:
Initializing class...
Entering context...
Code inside with statement
Exiting context...

The above shows that our context manager class is executed in the following sequence:
__init__ method
__enter__ method
The code in the with statement block
__exit__ method
"""

#Part 2 of CBC managers
class WorkWithFile:
  def __init__(self, file, mode):
    #3 parameters
    #file: need to be able to take file argument when we call class with a with statement
    #mode: need to provide a mode
    #Allow us to accomplish this: with WorkWithFile('file.txt', 'r')
    self.file = file
    self.mode = mode
 
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    #Any new instance of cm will have file and mode property, we can pass them into open() to open a file with a specifif mode
    return self.opened_file
    #by returning this, the file will be passed into the variable we define when we use with satement
 
  def __exit__(self, *exc):
    self.opened_file.close()

# Write your code below:
class PoemFiles:
  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode
  
  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
  
  def __exit__(self, *exc):
    print('Closing poem file')
    self.opened_poem_file.close()

with PoemFiles('poem.txt', 'w') as open_poem_file:
  open_poem_file.write('Hope is the thing with feathers')
  

#Handling exceptions
"""
The exit function is responsible for handling functions

If we did this: def __exit__(self):, we would get an error:
__exit__() takes 1 positional argument but 4 were given.

This is because exit() requires four total arguments. In past exercises we ignored this requirement by using * operator 
to tell this method we will pass a variable number of arguments even though we never did

__exit__ method takes 3 required aruments in addition to self

1. An exception type: which indicates the calss of exception (AttributeError, NameError, etc.)
2. An exception value: the actual value of the error
3. A traceback: a report detailing the sequence of steps that caused the error and all the details needed to fix the error
"""

class OpenFile:
 
 def __init__(self, file, mode):
   self.file = file
   self.mode = mode

 def __enter__(self):
   self.opened_file = open(self.file, self.mode)
   return self.opened_file
 
 def __exit__(self, exc_type, exc_val, traceback):
   print(exc_type)
   print(exc_val)
   print(traceback)
   self.opened_file.close()

with OpenFile("file.txt", "r") as file:
  # .see() is not a real method
  print(file.see())
  
"""
Output: 
<class 'AttributeError'>
'_io.TextIOWrapper' object has no attribute 'see'
<traceback object at 0x7f08dcfb5040>

Traceback (most recent call last):
  File "script.py", line 14, in <module>
    print(file.see())
AttributeError: '_io.TextIOWrapper' object has no attribute 'see'

Once the with statement is run, we get the above error message that tells us that we have an AttributeError, 
that our object has no attribute 'see', and provides a traceback object.

When an error occurs, the code stops, and resources (like our file) are still closed. The value 
of these three arguments are then thrown or suppressed

If no error occurs in the with satement above, the exit method would print
None
None
None

Note:
Note that exc_type, exc_value, and traceback are completely 
arbitrary names. We can use any name we want for these parameters as 
long as it does not hinder the readability of our code. In general, it’s best practice to be as descriptive as possible!
"""

class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n ')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()

  # Create your __exit__ method here:

#First (Errors)
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())

# Second (No errors)
# with PoemFiles('poem.txt', 'r') as file2:
#   print(file2.read())
#   print("---- Exception data below ----")


#Handling exceptions II
"""
Handling exceptions in the __exit__ method isn't the only way we can handle it
An exception that occurs in the context manager can be handled in two ways:

If we want to throw an error when an error occurs, we can either:
    Return False after the .close() method
    Do nothing

If we want to suppress the error, we can:
    Return True after the .close() method
"""
class OpenFile:
 
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
 
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
 
  def __exit__(self, exc_type, exc_val, traceback):
    print(exc_type, exc_val, traceback)
    print("The exception has been handled")
    self.file.close()
    return True

with OpenFile("file.txt", "r") as file:
  # .see() is not a real method
  print(file.see())

with OpenFile("file.txt", "r") as file:
  print(file.read())


"""
Output:
<class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'see' <traceback object at 0x7fedf822d180>
The exception has been handled
None None None

In this example, both with statments are ran and there is no automatic error message thrown by the program
If we did not return True, the second (and all proceeding) with statements would not have run since an exception would be hit.

Also, we can choose to handle a specific exception, while also suppressing it! This is useful if we want our context manager
to not block the execution of other code, but also customize the output if a certain exception occurs. Here is an example of 
working with TypeError
"""
class OpenFile:
 
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
 
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
 
  def __exit__(self, exc_type, exc_val, traceback):
    self.file.close()
    if isinstance(exc_val, TypeError):
      # Handle TypeError here...
      print("The exception has been handled")
      return True
  
"""
Notice the if statement that compares exc_val to a specific exception we are trying to catch. 
Anything we want to happen for this specific exception can occur in the conditional code block. 
Lastly, we return True to make sure we suppress the exception from arising and stopping the rest of our code from running.

NOTE: Remember that the __exit__() method’s primary responsibility is to close the resource the context 
manager is working with. In this example, we close the file first, before handling the error, so that it will always execute.
"""
class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print(' \n --  Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Checkpoint 2
    self.opened_poem_file.close()
    if isinstance(exc_value, AttributeError):
      return True
    

with PoemFiles('poem.txt', 'r') as file:
  print("---- Exception data below ---- \n ")
  print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n ---- Exception data below ---- \n ")

#Contextlib
"""
Provides a simpler method for creating context managers

Allows for the creation of a context manager with the use of a generator function (a function that uses yield instead of return) and
the contextlib decorator -@contextmanager instead of creating a class and defining __enter__ and __exit__ methods
"""
from contextlib import contextmanager
from contextlib import contextmanager

@contextmanager
def open_file_contextlib(file, mode): #Wrap a simple generator function
    opened_file = open(file, mode)
    try:
        yield opened_file
    finally:
        opened_file.close()

"""
1.We have written a generator function called open_file_contextlib with the expectation that it will take in two arguments, a file and a mode.
2.We then use the built-in open() function to open the file (that we received as an argument) and save it to a variable called opened_file.
3.The function then will attempt (via a try statement) to yield the opened file Pand complete whatever code we 
pass when we use it in conjunction with the with statement. More on this in a bit!
4.Lastly the resource (file) will be closed once all the code is done being executed.
"""
# @contextmanager
# def generator_function(<parameters>):
#     <setup section - equivalent to __enter__ >
#     try:
#         yield <value>
#     finally:
#         <cleanup section - equivalent to __exit__ >

"""
After creating this function and denoting as a context manager using decorator, we can use it immediately in a with statement
"""
with open_file_contextlib('file.txt', 'w') as opened_file:
 opened_file.write('We just made a context manager using contexlib')

# Write your code below:
from contextlib import contextmanager


@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()


with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.write('Rose is beautiful, Just like you.')


#Contextlib  Error Handling
"""
Dealing with errors in the decorator method is done within the except block. There are typically 2 ways to handle errors

1. Throw an error and stop the execution of our entire program
    do nothing by excluding an except block
2. To catch errors and continue the execution of our program, we can:
    handle the exception via an except block
"""
from contextlib import contextmanager

@contextmanager
def open_file_contextlib(file, mode):
    open_file = open(file, mode)
    try:
        yield open_file
    except Exception as exception:
        print('We hit an error: ' + str(exception)) #attempts to catch generic exception, this line prints error
    finally:
        open_file.close()
    
    with open_file_contextlib('file.txt', 'w') as opened_file:
        opened_file.sign('We just made a context manager using contexlib')
#This will hit an error because .sign() file is not a file method
#Output:
#We hit an error: '_io.TextIOWrapper' object has no attribute 'sign'
from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  #Write your code below: 
  except AttributeError as e:
    print(e)
  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.sign('Buzz is big city. big city is buzz.')

"""
Output:
Opening File
Inside yield
'_io.TextIOWrapper' object has no attribute 'sign'
Closing File
"""

#Nested Context Managers
"""
We've been looking at use of context managers within the same file but not other scenarios that include working with multiple files
1. Work with information from multiple files
2. Copy the same information to multiple files
3. Copy information from on file to another

In order to accomplish this, context managers can be nested together in a with satement to manage multiple resources simultaneously
Let’s imagine we have two files: a teacher.txt file and a student.txt. 
We want to copy all the information on the student file to the teachers. Our code might look like this:
"""
with open('teacher.txt', 'w') as teacher, open('student.txt', 'r') as student:
 teacher.write(student.read())
 
"""
The with statement is being called once but invoking two context managers. This is a single-line nested with statement
Each context manager is separated by a comma and has its own target variable
Our teacher.txt file is being opened in write mode because it will be written into and our student.txt is read because we are
copying its text into teacher.txt

teacher.txt will have everything that student.txt has
In this example, we have decided to use open() instead of a custom context manager
"""
#Another way of doing it
with open("teacher.txt", "w") as teacher:
   with open("student.txt", "r") as student:
     teacher.write(student.read())
"""
In this example, the with statement is being called twice
The with statement to open student.txt is nested in the with statement that is being used to open teacher
This method gives a clearer visual of nesting and is preferable when working with more than two context managers
"""

from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File')
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File')
    open_card_file.close()

# Write your code below: 
with poem_files('poem.txt', 'r') as poem:
  with card_files('card.txt', 'w') as card:
    print(poem)
    print(card)
    card.write(poem.read())

