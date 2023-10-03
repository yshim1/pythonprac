#Any object that stores data is called a container
#built-in containers include lists or dictionairs

"""
Lists:
Lists are an ordered group of elements. Elements can be added, removed, accessed, and modified.

Tuples:
Tuples are immutable objects which group multiple elements together. They are similar to lists, 
except that they cannot be modified once created.

Dictionaries:
Dictionaries are unordered groups of key-value pairs.

Sets:
Sets are unordered groups of elements that cannot contain duplicates, elements cannot be modified.
"""
#List
products = ['t-shirt', 'pants', 'shoes', 'dress', 'blouse']
products.append('jacket')
products.sort()
products.remove('shoes')

#Tuple
searched_terms = ('clothes', 'phone', 'app', 'purchase', 'clothes', 'store', 'app', 'clothes')
term = searched_terms[2]
num_of_occurrences = searched_terms.count('clothes')

#Dictionary
orders = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}, 
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}
         }
order_4829_price = orders['order_4829']['price']
order_6184_size = orders['order_6184']['size']
orders['order_4829']['size'] = 'x-large'
num_of_orders = len(orders)

#Sets
old_products_set = {'t-shirt', 'pants', 'shoes'}
new_products_set = {'t-shirt', 'pants', 'blouse', 'dress'}
updated_products = new_products_set | old_products_set
removed_products = old_products_set - new_products_set


#Specialized Containers
from collections import *
import collections
from collections import OrderedDict

orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
          'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})

orders.move_to_end('order_4829')
orders.popitem()

"""
Names of some advanced containers include:
deque, namedtuple, Counter, defaultdict, OrderedDict, ChainMap

Names of container wrappers include:
UserDict, UserList, UserString
"""

#Deque

"""
Deques are helpful for appending and popping large amounts of data from both sides rather than being optimized for accessing on index (like lists are)
"""
from codefiles.helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
supplies_deque = deque()
ordered_important_supplies = deque()
for item in csv_data:
  if 'important' in item:
    supplies_deque.appendleft(item)
  else:
    supplies_deque.append(item)

for i in range(25):
  ordered_important_supplies.append(supplies_deque.popleft())

ordered_unimportant_supplies = deque()
for i in range(10):
  ordered_unimportant_supplies.append(supplies_deque.pop())
  

#Named Tuple
"""
Tuples are useful for grouping together data that does not need to be modified in the future. However, tuples run into issues
when they host various data and even nested data

namedtuples allow us to order our data by type within the tuple itself
"""
from collections import namedtuple
ActorData = namedtuple('ActorData', ['name', 'birth_year', 'movie', 'movie_release_date'])
actor_data = ActorData('Leonardo DiCaprio', 1974, 'Titanic', 1997)
print(actor_data.name) #>> returns leonardo dicaprio

"""
Notes:
1.CapWords convention is used when defining namedtuple because namedtuple returns a subclass and thus falls under the conventions we use
for classes
2.field_names argument can be a single string with each fieldname separated by whitespace and or commas
3.namedtuple is immutable and maintain their order while a dictionary does not and are more lightweight than dictionaries, they take
no more memory than a regular tuple

There are other useful methods that a namedtuple uses such as converting from a namedtuple to a dict, replacing elements and field names
and even setting default values for attributes
"""
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
from collections import namedtuple
ClothingItem = namedtuple('ClothingItem', 'type color size price')
new_coat = ClothingItem('coat', 'black', 'small', 14.99)
coat_cost = new_coat.price

updated_clothes_data = []
for item in clothes:
  updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))
  
#Default Dict
"""
By using a default dict, we can supply a default missing value for the dictionary so we won't run into many key errors

Note: 
we set a default value using a lambda expression. Any time we try to access a key that does not exist, it automatically
ipdates our default dict object by creating a new key-value pair using the missing key and default value
"""
from collections import defaultdict

validate_prices = defaultdict(lambda: 'No Price Assigned')
validate_prices['jeans'] = 19.99
validate_prices['shoes'] = 24.99
validate_prices['t-shirt'] = 9.99
validate_prices['blouse'] = 19.99
print(validate_prices['jacket'])

site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
from collections import defaultdict
validated_locations = defaultdict(lambda: 'TODO: Add to website')
validated_locations.update(site_locations)
for item in updated_products:
  site_locations[item] = validated_locations[item]

print(site_locations)


#OrderedDict
"""
Ordered Dict allows us to access values using keys, but it also preserves the order of elements inside of it
When using an OrderedDict, we can move an element to the back or front and pop the data from the back or front of the 
OrderedDict
"""
first_order = {'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}}
second_order = {'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}}
third_order = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}}
list_of_dicts = [first_order, second_order, third_order]
print(list_of_dicts[1]['order_6184']['price'])
"""
In order to get the price of a specific order, we must know the index of it already before we can access the
dictionary data stored inside:
"""

dict_of_dicts = {}
dict_of_dicts.update(first_order)
dict_of_dicts.update(second_order)
dict_of_dicts.update(third_order)
print(dict_of_dicts['order_6184']['price'])
"""
On the other hand, depending on the Python version, the dict container can preserve the order, but
it is difficult to move elements around:
"""
orders = OrderedDict()
orders.update({'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
orders.update({'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}})
orders.update({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}})
# Get a specific order
find_order = orders['order_2905']
# Get the data in a list format
orders_list = list(orders.items())
third_order = orders_list[2]
# Move an item to the end of the OrderedDict
orders.move_to_end('order_4829')
# Pop the last item in the dictionary
last_order = orders.popitem()

"""
Note:
these two methods accept boolean arguments which determine if element is moved/popped from the front or back of the ordereddict
"""
from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!
from collections import OrderedDict

orders = OrderedDict(order_data)
to_move = []
to_remove = []
for item in order_data:
  if item[1] == 'returned':
    to_move.append(item[0])
  elif 'canceled' in item:
    to_remove.append(item[0])

for item in to_remove:
  orders.pop(item)
for item in to_move:
  orders.move_to_end(item)
print(orders)

#ChainMap
"""
Alows us to store many mappings in an ordered group, but looksups (accessing the value using a key) are repeated for every mapping
inside ChainMap until something is found or the end is reached

If we try to modify the data in any way, then only the first mapping in the ChainMap will receive the changes. When accessing data,
one way to think of the ChainMap is that it treats all of the stored dictionaries as one large dictionary, where if there are repeated keys,
then the first found result is returned
"""
from collections import ChainMap

customer_info = {'name': 'Dmitri Buyer', 'age': '31', 'address': '123 Python Lane', 'phone_number': '5552930183'}
shirt_dimensions = {'shoulder': 20, 'chest': 42, 'torso_length': 29}
pants_dimensions = {'waist': 36, 'leg_length': 42.5, 'hip': 21.5, 'thigh': 25, 'bottom': 18}
customer_data = ChainMap(customer_info, shirt_dimensions, pants_dimensions)
customer_size_data = customer_data.parents #>>Output will be shirt_dimensions dict and pants_dimensions dict which are parents of first mapping
customer_data['address'] = '456 ChainMap Drive' #>>We can directly modify the data only in the first dictionary

"""
Note: In order to modify data from dictionaries which are deeper in the ChainMap, we will need 
to iterate through the dictionaries which are stored inside of it.

Another interesting concept that the ChainMap uses is the concept of a parent mappings.
If we use the .parents property, all mappings except the first one will be returned. 
This is because those mappings are considered to be the parent mappings to the first one. 
You can add a new “child” mapping to the front of the list of mappings using the .new_child() method.
"""


year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!
from collections import ChainMap
profit_map = ChainMap(*year_profit_data) #Unpacking operator
def get_profits(input_map):
  a, b = 0, 0
  for key, value in input_map.items():
    if 'holiday' in key:
      b+= value
    else:
      a+= value
  return a, b

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

for item in new_months_data: #Why not use unpacking operator here?
  profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

year_diff_standard_profit, year_diff_holiday_profit = (current_year_standard_profit - last_year_standard_profit), (current_year_holiday_profit - last_year_holiday_profit)

#Counter
"""
Counter container instantly counts elements for any hashable object. It stores the data as a dictionary where the keys are 
elements and the values are the number of occurrences. 
"""
clothes_list = ['skirt', 'hoodie', 'dress', 'blouse', 'jeans', 'shoes', 'skirt', 'skirt', 'jeans', 'hoodie', 'boots', 'jeans', 'jacket', 't-shirt', 'skirt', 'skirt', 'dress', 'shoes', 'blouse', 'hoodie', 'skirt', 'boots', 'shoes', 'boots', 'jeans', 'hoodie', 'blouse', 'hoodie', 'shoes', 'shoes', 'blouse', 'boots', 'blouse', 'hoodie', 't-shirt', 'jeans', 'dress', 'skirt', 'jacket', 'boots', 'skirt', 'dress', 'jeans', 'jeans', 'jacket', 'jeans', 'shoes', 'dress', 'hoodie', 'blouse']

from collections import Counter
counted_items = Counter(clothes_list)
print(counted_items)


opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code below!
from collections import Counter

def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]

tshirts_sold=find_amount_sold(opening_inventory, closing_inventory, 't-shirt')
print(tshirts_sold)


#Container Wrappers
"""
Container wrappers are modifications to functions or classes which change the behavior in some way. They are called wrappers because
they wrap around existing code to modify it. This is most commonly used with the function wrapping, but we can also wrap classes

Wrapper classes allow us to create different variations of classes with different purposes while avoiding duplicate code.
Since we use an instance of the wrapped class inside of it, it preserves all of the attributes and methods from the wrapped class
and keeps us from having to retype all of the code

The collections class has 3 different wrapper classes set up for us to modify: UserDict, UserList, UserString
"""

#UserDict
"""
The UserDict container wrapper lets us create our own version of a dictionary. The functionality is the same as a normal dict
but we can access the dictionary data through the data property
"""
from collections import UserDict

# Create a class which inherits from the UserDict class
class DisplayDict(UserDict):
    # A new method to increase the dictionary's functionality
    def display_info(self):
        print("Number of Keys: " + str(len(self.keys())))
        print("Keys: " + str(list(self.keys())))
        print("Number of Values: " + str(len(self.values())))
        print("Values: " + str(list(self.values())))

    # We can also overwrite a method from the dictionary class
    def clear(self):
        print("Deleting all items from the dictionary!")
        super().clear()

disp_dict = DisplayDict({'user': 'Mark', 'device': 'desktop', 'num_visits': 37})
disp_dict.display_info()
disp_dict.clear()

"""
As shown in this example, we can add methods and override methods from the UserDict class. This is the same as inheriting from 
regular classes
"""

"""
Note that you cannot pop from a dictionary while iterating because the dictionary size cannot change while iterating
"""

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
from collections import UserDict

class OrderProcessingDict(UserDict):
  def clean_orders(self):
    to_del = []
    for key, val in self.data.items():
      if val['order_status'] == 'complete':
        to_del.append(key)
    
    for item in to_del:
      del(self.data[item])

process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)

#UserList
"""
Similar to UserDict but for lists. Just like in UserDict, it has a property called data for us to access the list contents directly
"""
from collections import UserList

# Create a class which inherits from the UserList class
class CondenseList(UserList):

    # A new method to remove duplicate items from the list
    def condense(self):
        self.data = list(set(self.data))
        print(self.data)


    # We can also overwrite a method from the list class
    def clear(self):
        print("Deleting all items from the list!")
        super().clear()

condense_list = CondenseList(['t-shirt', 'jeans', 'jeans', 't-shirt', 'shoes'])
condense_list.condense()
condense_list.clear()


data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
from collections import UserList

class ListSorter(UserList):
  def append(self, item):
    super().append(item)
    self.sort()

sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)

#UserString
"""
Similar to UserList and UserDict. Has data property to access string's data
"""
from collections import UserString

# Create a class which inherits from the UserString class
class IntenseString(UserString):

    # A new method to capitalize and add exclamation points to our string
    def exclaim(self):
        self.data = self.data.upper() + '!!!'
        return self.data


    # Overwrite the count method to only count a certain letter
    def count(self, sub=None, start=0, end=0):
        num = 0
        for let in self.data:
            if let == 'P':
                num+=1
        return num


intense_string = IntenseString("python rules")
print(intense_string.exclaim())
print(intense_string.count())


str_name = 'python powered patterned products'
str_word = 'patterned '

# Write your code below!
from collections import UserString
class SubtractString(UserString):
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other,'')


subtract_string = SubtractString(str_name)
subtract_string - str_word

from collections import *

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# Write your code below!

# Checkpoint #1
split_prices = deque()

#Checkpoint #2
for item in overstock_items:
  if item[1] > 20.0:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)
print(split_prices)

# Checkpoint #3
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

# Checkpoint #4
bundles = []
while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(),split_prices.popleft()]

  calc_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

# Checkpoint #5
promoted_bundles = []
for bundle in bundles:
  if bundle.bundle_price > 100:
    promoted_bundles.append(bundle)

# # Checkpoint #6
print(promoted_bundles)

# for bundle in promoted_bundles:
#   print(bundle)    


#Quiz Questions
"Which of the following choices is NOT a valid way of setting a default value for a defaultdict?"
#1
default = defaultdict(lambda:'default string')
#2
default = defaultdict(str)
#3
def get_default_value():
    return 'default string'
default = defaultdict(get_default_value)
#4
default = defaultdict('default string')
#Answer is 4
