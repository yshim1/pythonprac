#Generator functions
#Similar to regular functions except that they must return an iterator. Instead of using return statement, yield expression is used

#Difference between yield and return?
#The code after the yield expression will execute on the next iteration of the iterator. Code after return statement will not execute

def course_generator():
  yield 'Computer Science'
  yield 'Art'
  yield 'Business'

courses = course_generator()
for course in courses:
    print(course)
#>> Output:
#Computer Science
#Art
#Business

#Another key difference between yield and return is that the yield expression will suspend the execution of the function and preserve any
#local variables that exist within the function.
#The return statement will terminate function immediately and return the result(s) to the caller

#Like all objects, the iterator object returned by the generator function can be stored in a variable to be used later
# Write your code below: 
def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

class_standings = class_standing_generator()
for item in class_standings:
  print(item)

#next() and StopIteration
"""
Generator functions return an iterator object that contains traversable values. Retrieving values an be done by next() which will
cause generator function to resume until next yield expression is found. After it is found, the function will pause again

If no yield expression is found, code is finished and StopIteration is raised

Generator functions are not limited to just single yield statements. They also include loops where the yield occurs
"""

def prize_generator():
  student_info = {
    "Joan Stark": 355,
    "Billy Mars": 45,
    "Tori Rivers": 18,
    "Kyle Newman": 25
  }

  for student in student_info:
    name = student
    id = student_info[name]
    if id % 3 == 0 and id % 5 == 0:
      yield student + " gets prize C"
    elif id % 3 == 0:
      yield student + " gets prize A"
    elif id % 5 == 0:
      yield student + " gets prize B"
      
"""
student_info is preserved while the function executes with each next() call. We can see this by creating a variable prizes that calls
the prize_generator() function and then calling next() on it
"""
prizes = prize_generator()
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))

def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Write your code below:
  for i in range(len(student_standings)):
    if student_standings[i] == 'Freshman':
      yield 500

standings = student_standing_generator()
print(next(standings))
print(next(standings))
print(next(standings))

def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Write your code below:
  for item in student_standings:
    if item == 'Freshman':
      yield 500
  
  standing_values = student_standing_generator()
  print(next(standing_values))
  print(next(standing_values))
  print(next(standing_values))
  

#Generator Expressions
"""
Allow for a clean, single-line definition and creation of an iterator. By using a generator expression, 
there is no need to define a full generator function as we covered in the previous exercises

V similar to list comprehensions but instead...
1.Returns a newly defined iterator
2.Uses parenthesis
"""
# List comprehension
a_list = [i*i for i in range(4)]

# Generator comprehension
a_generator = (i*i for i in range(4))

print(a_list)
print(a_generator)

def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Write your code below:
cs_courses = cs_generator()
for item in cs_courses:
  print(item)

cs_generator_exp = ('Computer Science ' + str(i) for i in range(1,5))
for item in cs_generator_exp:
  print(item)
  
#Generator Methods: send()
"""
The .send() method allows us to send a value to a generator using the yield expression. If you assign yield to a variable the argument
passed to the .send() method will be assigned to that variable. Calling .send() will also cause the generator to perform an iteration
"""
def count_generator():
  while True:
    n = yield
    print(n)

my_generator = count_generator()
next(my_generator) # 1st Iteration Output: 
next(my_generator) # 2nd Iteration Output: None
my_generator.send(3) # 3rd Iteration Output: 3
next(my_generator) # 4th Iteration Output: None

"""
In the code example above, the generator definition contains the line n = yield. 
This assigns the value in yield to n which will be None unless a value is passed using .send().

1.The 1st iteration creates no output since the execution stops at n = yield which is before print(n).
2.The 2nd iteration assigns None to n through the n = yield expression. None is printed.
3.The 3rd iteration is caused by my_generator.send(3). The value 3 is passed through yield and assigned to n. 3 is printed.
4.The last, and 4th, iteration, assigns None to n. None is printed.
"""

def generator():
  count = 0
  while True:
    n = yield count
    if n is not None:
      count = n
    count += 1

my_generator = generator()
print(next(my_generator)) # Output: 0
print(next(my_generator)) # Output: 1
print(my_generator.send(3)) # Output: 4
print(next(my_generator)) # Output: 5

"""
In the above example, the generator function defines count = 0 as the iteration value. n is used to hold the value provided by yield
Just like next(), send() returns the value of the recent iteration.

n= yield count has 2 behaviors:
1. At the start of each iteration the value provided by yield is assigned to n. This will be None when next() causes an iteration
or it will be equal to value passed using .send()
2. At the end of each iteration, the value stored in count is returned by the generator

If n is not None the value stored in n can be assigned to the iterator variable, count. This allows the iterator to only change the value
of count when .send() method is called
"""

MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    # Write your code below
    n = yield student_id
    if n is not None:
      student_id = n
      continue
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  if i == 1:
    i = student_id_generator.send(25)
  
  print(i)
  
#Generator methods: throw()
"""throw () provides the ability to throw an exception inside the generator from the caller point. This can be useful if we 
need the generator once it reaches a certain value or meets a particular condition"""
def generator():
  i = 0
  while True:
    yield i
    i += 1

my_generator = generator()
for item in my_generator:
    if item == 3:
        my_generator.throw(ValueError, "Bad value given")

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  # Write your code below:
  if student_id > 100:

    student_generator.throw(ValueError, 'Invalid student ID')
  print(student_id)
  
#close()
"""
close is used to terminate a generator early. Once the close method is called, the generator is finished just like the end of a 
for loop. Any further iteration attempts will raise a StopIteration exception
"""
def generator():
  i = 0
  while True:
    yield i
    i += 1

my_generator = generator()
next(my_generator)
next(my_generator)
my_generator.close()
next(my_generator) # raises StopGenerator exception

"""
close() method works by raising a GeneratorExit exception inside the generator function. The exception is generally ignored but can be 
handled by using try and except
"""
def generator():
  i = 0
  while True:
    try:
      yield i
    except GeneratorExit:
      print("Early exit, BYE!")
      break
    i += 1

my_generator = generator()
for item in my_generator:
  print(item)
  if item == 1:
    my_generator.close()
"""
Putting the yield expression in a try block can gandle the GeneratorExit exception. In this case, we print out a message
because we interrupted the automatic behavior of the .close() method. We must also use a break to exit the loop or else
a RuntimeError will occur
"""
def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  # Write your code below:
  if student_id > 99:
    student_generator.close() #Stops the code when the iteration reaches 100 because we originally start at 1
    
#Connecting Generators
"""
There are cases where it is useful to connect multiple gnerators into one. This allow sus to delegate the operations
of one generator to another sub-generator. Connecting generators is similar to using itertools chain() function
to combine iterators into a single iterator

In order to connect, we use the yield from statement
"""
def cs_courses():
    yield 'Computer Science'
    yield 'Artificial Intelligence'

def art_courses():
    yield 'Intro to Art'
    yield 'Selecting Mediums'


def all_courses():
    yield from cs_courses()
    yield from art_courses()

combined_generator = all_courses()

"""
1. We have a generator function called cs_courses() that yields two results, 'Computer Science' and 'Artificial Intelligence'.
2. We have another generator function called art_courses() that will yield two separate results, 'Intro to Art' and 'Selecting Mediums'.
3. Our all_courses() generator function will yield results from both cs_courses() and art_courses() to create one combined generator
with all four string values representing the courses.
"""

print(next(combined_generator)) #Computer Science
print(next(combined_generator)) #Artificial Intelligence
print(next(combined_generator)) #Intro to Art
print(next(combined_generator)) #Selecting Mediums

def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i
  
# Write your code below
def combined_students():
  yield from science_students(5)
  yield from non_science_students(10, 15)
  yield from non_science_students(25,30)

student_generator = combined_students()
for student in student_generator:
  print(student)
  
#Generator Pipelines
"""
Allows us to use multiple generators to perform a series of operations all within one expression. We can break down complex oeprations
into smaller, more manageable parts where they can then be pipelined together to achieve the desired output

In order to do so, the output of one generator function can be the input of another generator function. That resulting generator
can then be used as input for another generator function ad so on

Pipeline generators are also referred to as nested generators
"""

def number_generator():
  i = 0
  while True:
    yield i
    i += 1
    
def even_number_generator(numbers):
  for n in numbers:
    if n % 2 == 0:
      yield n

even_numbers = even_number_generator(number_generator())

for e in even_numbers:
  print(e)
  if e == 100:
    break

"""
The above example contains:

1. The infinite generator number_generator() that yields numbers incrementing by 1
2. The infinite generator even_number_generator() which takes a generator as a parameter, iterates through 
that generator and only yields even numbers.
3. The even_numbers variable which holds an even_number_generator() object with number_generator() as its argument.
"""

def course_generator():
    yield ("Computer Science", 5)
    # Write your code below:
    yield ('Art', 10)
    yield ('Business', 15)

def add_five_students(courses):
  for x in courses:
    yield (x[0], x[1] + 5)

increased_courses = add_five_students(course_generator())

for a in increased_courses:
  print(a)
  
  
def summa():
    yield 'Summa Cum Laude'

def magna():
    yield 'Magna Cum Laude' 

def cum_laude():
    yield 'Cum Laude'

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()


def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1


days = 25
countdown_generator = (day for day in range(days, -1,-1))
grad_days = graduation_countdown(days)
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print("Days Left: " + str(day))


days = 25
gpas = [3.2, 4.0, 3.6, 2.9]
honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)