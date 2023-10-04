#Lambda function also called anonymous functions
def add_two(my_input):
  return my_input + 2

add_two = lambda my_input: my_input + 2

"""
1. The function is stored in a variable called add_two
2. The lambda keyword declares that this is a lambda function (similar to how we use def to declare a normal function)
3. my_input is a parameter used to hold the value passed to add_two
4. In the lambda function version, we are returning my input + 2 without use of return keyword
"""

#another example
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'