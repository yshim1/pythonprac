#__iter__() and iter()
"""
Iterator objet is a special object that represents a stream of data that we can operate on. To acomplish this,
it uses a built in function called iter()
"""

#iterable
dog_foods = {
    "Great Dane Foods": 4,
    "Min Pin Pup Foods": 10,
    "Pawsome Pups Foods": 8
}
#iteration
for food_brand in dog_foods:
    print(food_brand + " has " + str(dog_foods[food_brand]) + " bags")

dog_food_iterator = iter(dog_foods)
print(dog_food_iterator)  #>> <dict_keyiterator object at 0x7f78f8077ae0> is output

#for loop uses iter() function to convert dog_foods into iterator object

#Behind the scences, iter(dog_foods) is calling a method defined within the iterable called __iter__()
#All iterables have __iter__() method defined. We can even use the python built-in function dir() to show
#that our dog_foods dictionary (iterable) has a defined method called __iter__()

print(dir(dog_foods))

# dog_foods.__iter__() will retrieve same object as iter(dog_foods)

sku_list = [7046538, 8289407, 9056375, 2308597]

# Write your code below:

print(dir(sku_list))
sku_iterator_object_one = sku_list.__iter__()
print(sku_iterator_object_one)

sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)

#next() and __next__(): very similar to iter() and __iter__()
sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
next_sku = sku_iterator.__next__()
print(next_sku)

sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
next_sku = next(sku_iterator)
print(next_sku)

sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
for i in range(5):				#How does the iterator object know when to stop??
  next_sku = sku_iterator.__next__()
  print(next_sku)
#__next__() method will raise an exception called StopIteration when all items have been iterated through

dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

# Write your code below:
dog_food_iterator = iter(dog_foods)
next_dog_food1 = next(dog_food_iterator)
print(next_dog_food1)

next_dog_food2 = next(dog_food_iterator)
print(next_dog_food2)

next_dog_food3 = next(dog_food_iterator)
print(next_dog_food3)

next(dog_food_iterator)

#Iterators and For Loops
"""
dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}
for food_brand in dog_foods:
  print (food_brand + " has " + str(dog_foods[food_brand]) + " bags")

Steps:
1.The for loop will first retrieve an iterator object for the dog_foods dictionary using iter().

2.Then, next() is called on each iteration of the for loop to retrieve the next value. This value is set to the for loop’s variable, food_brand.

3.On each for loop iteration, the print statement is executed, until finally, the for loop executes a call to next() that raises the StopIteration exception. The for loop then exits and is finished iterating.
"""

#Iterator Protocol: The implementation of __iter__() and __next__() to make an object an iterator object
#Custom iterator objects
class FishInventory:
  def __init__(self, fishList):
      self.available_fish = fishList

fish_inventory_cls = FishInventory(["Bubbles", "Finley", "Moby"])

# Write your code below:
for fish in fish_inventory_cls:
  pass

#In order to create an iterator object, we must implement __iter__() and __next__() methods in our class def

#Custom Iterators II

#__iter__():
	#method must always return iterator object itself (self). Can also include some class member initializing
 #__next__():
	#method must either return the next value available or raise the StopIteration exception. Can include any number of operations
class FishInventory:
    def __init__(self, fishList):
        self.available_fish = fishList
    
    def __iter__(self):
        self.index = 0 #index will help us track the current position we're in within self.available_fish list
        return self #returns self because this class is the iterator object, __iter__() method can return other iterator objects
					# but typically the object itself is returned here by using return self
    
    # def __next__(self):
    #     fish_status = self.available_fish[self.index] + " is available!"
    #     self.index += 1
    #     return fish_status
    def __next__(self):
        if self.index < len(self.available_fish):
            fish_status = self.available_fish[self.index] + " is available!"
            self.index += 1
            return fish_status #Must return something
        else:
            raise StopIteration
class CustomerCounter:
# Write your code below:

  def __iter__(self):
    self.count = 0
    return self
  
  def __next__(self):
    if self.count > 100:
      raise StopIteration
    else:
      self.count += 1
      return self.count

customer_counter = CustomerCounter()
for item in customer_counter:
  print(item)

    
#Python's itertools: Built-in iterators
	#A built-in module that provides the abilit to create complex iterator manipulations. These operations can input either a single
	#iterable or a combination of them
		#Infinite:
			#will repeat an infinite number of times. Will not raise StopIteration and will require a stop condition
		#Input-dependent:
			#are terminated by the input iterable(s) sequence length. Smallest length iterable parameter of an input-dependent iterator
			#will terminate the iterator
		#Combinatoric
			#iterators that are combinational, where math funcions are performed on the input iterables
import itertools

#Infinite iterator: Count
	#infinite iterators are useful when we have unbounded streams of data to process

#A useful itertool that is an infinite iterator is count() intertool. This infinte iterator will count from a first value
#until we provide some stop condition
	#base syntax
	#count(start, [step])
for i in itertools.count(start=0, step=2):
  print(i)
  if i >= 20:
    break

#Write your code below:
import itertools
max_capacity = 1000
num_bags = 0

for i in itertools.count(start=13.5, step=13.5): #i starts with weight of 1 bag and increments by 1 bag until max capacity hit
  if i > max_capacity:
    break
  num_bags+=1	#each iteration adds a bag

print(num_bags)

#Input-dependent iterator: chain
"""
An input-dependent iterator will terminate based on the length of one or more 
input values. They are great for working with and modifying existing iterators.
"""
#chain() takes in one or more iterables and combine them into a single iterator
	#Base Syntax:
	#chain(*iterables)
#The input for chain is one or more iterables of the same or varying iterable types
#Ex: we can use the chain itertool to combine a list and a set into one iterator

import itertools

odd = [5, 7, 9]
even = {6, 8, 10}

all_numbers = itertools.chain(odd, even)

for number in all_numbers:
  print(number)
#<<Output:
# 5
# 7
# 9
# 8
# 10
# 6
"""
The output is finite since the input iterables, odd and even are also finite.
Note that Python sets are not ordered so the last 3 numbers in this example’s 
output will not always be in the initialized order.
"""

#Combaniatoric Iterator: Combinations
"""
Will perform a set of statistical or mathematical operations on an input iterable
combinations: will produce an iterator of tuples that contain combinations of all elements in the input
"""

#Basic syntax
#combinations(iterable, r)
	#Two arguments, first is iterable, second value r represents the length of each combination tuple
#return type is an iterator that can be used in a for loop or can be converted to iterable type using list() or set()
import itertools
even = [2, 4, 6]
even_combinations = list(itertools.combinations(even, 2))
print(even_combinations)
#This code will take an even list of numbers and return list of all combinations of 2 even numbers

import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# Write your code below: 
collar_combo_iterator = itertools.combinations(collars, 3)
for x in collar_combo_iterator:
  print(x)

#Review
# Write your code below:
import itertools
cat_toys = [('laser', 1.99), ('fountain', 5.99), ('scratcher', 10.99), ('catnip', 15.99)]
cat_toy_iterator = iter(cat_toys)
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
max_money = 15
options = []
toy_combos = itertools.combinations(cat_toys, 2)

for combo in toy_combos:
   toy1 = combo[0]
   cost_of_toy1 = toy1[1]
   toy2 = combo[1]
   cost_of_toy2 = toy2[1]
   cost = cost_of_toy1 + cost_of_toy2
   if cost < max_money:
    options.append(combo)
print(options)

#Which of the following is NOT a way that for loops utilize iterators?

#Wrong Selected Answer: The for loop terminates when a next() call raises a StopIteration exception
#Correct Answer: The for loop implements the iterator protocol for the iterable object
