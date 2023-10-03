#Using Unpacking Operator
#The * assigns each number to an argument in the function definition
my_num_list = [3, 6, 9]

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

sum(*my_num_list)


numbers  = {'num1': 3, 'num2': 6, 'num3': 9}
sum(**numbers)

#Using operator within built in function i.e. range()
start_and_stop = [3, 6]
range_values = range(*start_and_stop)
print(list(range_values))

#Unpacking parts of an iterable
a, *b, c = [3, 6, 9, 12, 15]
print(b)

#Merging iterables
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)
#>>(0, 3, 6, 9, 12)


num_list = [1,2,3,4,5,6,7,8]

def power_two(*nums):
    for num in nums:
        print(num**2)
power_two(*num_list)


