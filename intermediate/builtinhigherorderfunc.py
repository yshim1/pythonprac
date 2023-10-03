#3 common higher order functions
"""
map()
filter()
reduce()
"""

#Syntax of map
#returned_map_object = map(function, iterable)
"""
Applies the passed function to each and every element in the iterable and returns a map object. The returned map object
holds the results from applying the mapping function to each element in the passed iterable. To view the map object, we convert
the map object to a list. Map works well with lambda functions

Example bellow:
"""
def double(x):
    return x*2
l = [1,2,3,4,5,6]
a = map(double, l)
print(a)
print(list(a))
"""<<Can also be written as lambda function"""
a2 = map(lambda x: x*2, l)
print(list(a2))

grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:

# assign the result of your map function to the variable grades_100scale
grades_100scale = map(lambda x: x*25 if x < 4.0 else x, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list 
updated_grade_list = list(grades_100scale)
# print updated_grade_list
print(updated_grade_list)


#filter()
"""
filter(function, iterable)
Applies a passed filtering function to each element in the passed iterable. The filtering function should be a function 
that returns a boolean value. The returned filter object will only hold the True elements

Example below:
"""
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
 
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
 
print(list(M_names))

books = [["Burgess", 1985],
 ["Orwell", "Nineteen Eighty-four"],
  ["Murakami", "1Q85"],
   ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
     ["Murakami", 1985]]

# Your code below: 

# assign the result of your filter function to the variable  string_titles
string_titles = filter(lambda x: type(x[1])==str, books)
# convert your filter object to a list stored in the variable string_titles_list
string_titles_list=(list(string_titles))

# print the list string_titles_list
print(string_titles_list)

#Reduce()
"""
Reduce() function must be imported from functools. It is not built in like map and filter
Rather than returning a reduce object, it returns a single value. It cumulatively applies a
passed function to each sequential pair of elements in an iterable
"""

from functools import reduce
int_list = [3,6,9,12]

reduced_int_list = reduce(lambda x,y: x*y, int_list)
print(reduced_int_list)
"""
1.The reduce() function applies the lambda function to the first two elements in the list, 3 and 6, to get a product of 18.
2.Next, 18 was multiplied by the following element in the list, 9, to get 162.
3.Continuing on, 162 was multiplied by the next element, 12, to get 1944.
"""
letters = ['r', 'e', 'd', 'u', 'c', 'e']
# your code below:
# remember to import the reduce function
from functools import reduce
# store the result of your reduce function in the variable word
word = reduce(lambda x,y: x+y, letters)
# print word
print(word)