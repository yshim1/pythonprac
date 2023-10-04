#Function arguments
"""
There are three common types of function arguments

Positional arguments: arguments that are called by their position in the function definition
Keyword arguments: arguments that are called by their name
Default arguments: arguments that are given default values
"""

#Unlimited number of arguments
print('I', 'can', 'have', 'any', 'amount', 'of', 'arguments')

"""
The unpacking operator allows us to give our function a variable number of arguments by performing what's known as positional argument
packing

Whatever name follows the unpacking operator will store the arguments passed into the function in the form of a tuple. This allows our
functions to accept any number of arguments such as print()
"""
def my_function(*args):
  print(args)

def shout_strings(*args):
  for argument in args: #args becomes a tuple
    print(argument.upper())

shout_strings('Working on', 'learning', 'argument unpacking!')

def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length]) #Uitilizing * and regular positional argument

truncate_sentences(8, "What's going on here", "Looks like we've been cut off")


"""
Unlimited keyword arguments
"""
def arbitrary_keyword_args(**kwargs):
  print(type(kwargs)) #Output>> dict
  print(kwargs)
  # See if there's an 'anything_goes' keyword arg and print it
  print(kwargs.get('anything_goes')) #Outputs 101

arbitrary_keyword_args(this_arg='wowzers', anything_goes=101) 

"""
**kwargs takes the form of a dictionary with all the keyword parameter as keys and the argument as the value in the dictionary
Its important to note that positional arguments must come before **kwargs otherwise it would be a syntax error

The order is (positional args, *args, kwargs, **kwargs)
"""

#Using Unpacking Operator
#The * assigns each number to an argument in the function definition
my_num_list = [3, 6, 9]

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

sum(*my_num_list) #Spreads contents of num list into individual arguments in our function definition


numbers  = {'num1': 3, 'num2': 6, 'num3': 9}
sum(**numbers)

#Using operator within built in function i.e. range()
start_and_stop = [3, 6]
range_values = range(*start_and_stop)
print(list(range_values)) #OUTPUT>> [3,4,5]

#Unpacking parts of an iterable
a, *b, c = [3, 6, 9, 12, 15]
print(b) #OUTPUT>> [6,9,12]

#Merging iterables
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)
#>>(0, 3, 6, 9, 12)


num_list = [1,2,3,4,5,6,7,8]

def power_two(*nums):
    for num in nums:
        print(num**2)
power_two(*num_list) #OUTPUT: 9 36 81 each on new lines


def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

# Write your code below: 
table_7_total = [534.50, 20.0, 5]
calculate_price_per_person(*table_7_total)