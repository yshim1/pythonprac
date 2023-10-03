"""
All functions are classified as First class Objects meaning...

First-class objects can be stored as variables.
First-class objects can be passed as arguments to a function.
First-class objects can be returned by a function.
First-class objects can be stored in data structures (e.g., lists, dictionaries, etc.).

This means we can write powerful types of functions called higher-order functions
"""

#Higher Order Functions
"""
Operate on other functions via arguments or via return values. This means higher-order functions do one of both of the following
1. Accept a function as an argument
2. Have a return value that is a function
"""
def total_bill(func, value):
    total = func(value)
    return (f'The total amount owed is ${total}. Thank you! :)')


def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total

def add_tip(total):
    tip = total * .2
    new_total = total + tip
    return new_total

print(total_bill(add_tip, 100), total_bill(add_tax, 100))


#Functions as Arguments - Iteration
bills = [115, 120, 42]
 
new_bills = []
 
for i in range(len(bills)):
    total = add_tax(bills[i])
    new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

print(new_bills)

def total_bills(func, list):
  # This list will store all the new bill values
    new_bills = []

  # This loop will iterate through our bills
    for i in range(len(list)):

    # Here we apply the function to each element of the list!
        total = func(list[i])
        new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

    return new_bills

#functions as return values
"""
A function that returns another function is a higher-order function
"""
def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,        
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length*width*height

    return volume
 
box_volume_height15 = make_box_volume_function(15)
 
print(box_volume_height15(3,2))
