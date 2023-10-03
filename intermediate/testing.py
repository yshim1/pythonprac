"""
Two types of testing that exist
Manual testing: With manual testing, a physical person interacts with software
much as a user would. In fact, we have been manually testing our code any time 
we run it and observe the results!


Automated testing: With automated testing, tests are performed with code. 
Generally, automated testing is faster and less prone to human error.
"""

#Assert
#Syntax
#assert <condition>, 'Message if condition is not met'
def times_ten(number):
    return number * 100

result = times_ten(20)
assert result == 200, 'Expected times_ten(20) to return 200, instead got ' + str(result)

destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# Write your code below: 
assert destination in destinations,'Sorry, Small World currently does not fly to this destination!'
city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:
def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'

def test_row_40():
  assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

test_row_1()
test_row_20()
test_row_40()

#Unittest framework
import unittest
#provides test runner (a component that collects and executes tests and then provides results to the user)
#also provides many other tools for test grouping, setup, teardown, skipping, and other features that we'll soon learn aboute

def times_ten(number):
    return number * 100
class TestTimesTen(unittest.TestCase):
    pass
    def test_multiply_ten_by_zero(self): #unittest module requires that test function begin with the word test
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

    def test_multiply_ten_by_one_million(self):
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')

    def test_multiply_ten_by_negative_number(self):
        self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')

unittest.main() #This is how we run our tests
"""
Output:
FF.
======================================================================
FAIL: test_multiply_ten_by_negative_number (__main__.TestTimesTen)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/yamlak/Documents/pythonprac/p1.py", line 16, in test_multiply_ten_by_negative_number
    self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')
AssertionError: -1000 != -100 : Expected add_times_ten(-10) to return -100

======================================================================
FAIL: test_multiply_ten_by_one_million (__main__.TestTimesTen)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/yamlak/Documents/pythonprac/p1.py", line 13, in test_multiply_ten_by_one_million
    self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')
AssertionError: 100000000 != 10000000 : Expected times_ten(1000000) to return 10000000

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=2)
"""

# your code below:
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:

class NearestExitTests(unittest.TestCase):
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1),'front', 'The nearest exit to row 1 is in the front!')

  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20),'middle', 'The nearest exit to row 20 is in the middle!')

  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40),'back', 'The nearest exit to row 40 is in the back!')

unittest.main()

#Assert Methods
    #self.assertEqual(value1, value2)
        #Takes 2 values as arguments and checks that they are equal, if not test fails
        
    #self.assertIn(value, container)
        #Checks that the first argument is found in the second argument, which should be a container. If it is not found, test fail
    
    #self.assertTrue(value)
        #Takes single arg, checks that the arg evaluates to True. If not true, the test fails


#Assert methods II: Quantitative Methods
    #self.assertLess(value1, value2)
        #Takes 2 arguments and checks if first is less than second, if not, test fails
    
    #self.assertAlmostEqual(value1, value2)
        #Takes 2 arguments and checks that their difference, when rounded to 7 decimal places, is 0. If values not close enough
        #test fails

#Assert methods III: Exception and Warning methods
    #self.assertRaises(specificException, function, functionArguments)
        #Takes an exception type as its first argument, a function reference as its second, and an arbitrary number of
        #arguments as the rest. Calls function, checks if exception raised as result, test passes if exception is raised
        #fails if no exception is raised. Can be used with custom exceptions
    
    #self.assertWarns(specificWarningException, function, functionArguments)
        #Takes warning type as first argument, a function reference as its second, and an arbitrary number of arguments for the rest
        #calls the function and checks that the warning occurs. Test passes if a warning is triggered and fails if it isn't
        
import unittest
import codefiles.alerts as alerts

# Write your code here:
class SystemAlertTests(unittest.TestCase):
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
  
  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)
    

unittest.main()

#Test parametrization
    #Tests with minor differences. Allows functionality of single test to get large amount of coverage of diff inputs
    #To accomplish test parametrization, the unittest framework provides us with the subTest context manager

import unittest

# The function we want to test
def times_ten(number):
    return number * 100

# Our test class
class TestTimesTen(unittest.TestCase):
    
    # A test method
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest():    #By using subtest, each iteration is treated as an individual test
                expected_result = num * 10
                message = 'Expected times_ten(' + str(num) + ') to return ' + str(expected_result)
                self.assertEqual(times_ten(num), expected_result, message)

#Python will run the code inside of the context manager on each iteration, and if one fails, it will return
#the failure as a separate test case failure

#for num in [0, 1000000, -10]:  We can also put an arg within subtest to improve readability
  #with self.subTest(num):
#Doing this improves output from FAIL: test_times_ten (__main__.TestTimesTen) (<subtest>) to FAIL: test_times_ten (__main__.TestTimesTen) [1000000]

import unittest
import codefiles.entertainment as entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movies = entertainment.get_daily_movies()
    licensed_movies = entertainment.get_licensed_movies()

    # Write your code below:
    for movie in daily_movies:
      print(movie)
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)

unittest.main()

#Test Fixtures
#A mechanism for ensuring proper test setup (putting tests into a known state) and test teardown(restoring the state prior to test running)
#These guarantee that our tests are running in predictable conditions and thus the results are reliable
def power_cycle_device():
  print('Power cycling bluetooth device...')

class BluetoothDeviceTests(unittest.TestCase):
  def setUp(self): #Ensures device is in working state before running each test. This is a test setup method so its run b4 every test
    power_cycle_device()

  def test_feature_a(self):
    print('Testing Feature A')

  def test_feature_b(self):
    print('Testing Feature B')

  def tearDown(self): #Ensures device is in a working state before running each test
    power_cycle_device()

#There is nothing in the tests that would cause the bluetooth to stop working. It would be inefficient to power cycle
#the device before and after every test. Below is the code refactor so that setup and teardown only happen once -
#before and after ALL tests in the class are run
class BluetoothDeviceTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    power_cycle_device()

  def test_feature_a(self):
    print('Testing Feature A')

  def test_feature_b(self):
    print('Testing Feature B')

  @classmethod
  def tearDownClass(cls):
    power_cycle_device()

import unittest
import codefiles.kiosk as kiosk

class CheckInKioskTests(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    kiosk.power_on_kiosk()
  
  def setUp(self):
    kiosk.return_to_welcome_page()
  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Write your code below:
  @classmethod
  def tearDownClass(cls):
    kiosk.power_off_kiosk()

unittest.main()

#Skipping tests
#There are 2 ways to skip tests
    #@unittest skip decorator
    #skipTest() method
import sys

class LinuxTests(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_linux_feature(self):
        print("This test should only run on Linux")

    @unittest.skipIf(not sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_other_linux_feature(self):
        print("This test should only run on Linux")

#second option
import sys

class LinuxTests(unittest.TestCase):

    def test_linux_feature(self):
        if not sys.platform.startswith("linux"):
            self.skipTest("Test only runs on Linux")
            
#Skip decorators are more convenient and make it easy to see under what conditions the test is skipped
#When the conditions for skipping a test are too complicated to pass into a skip decorator, skipTest method is the recommended alt

import unittest
import codefiles.entertainment as entertainment

class EntertainmentSystemTests(unittest.TestCase):

  @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  @unittest.skipUnless(not entertainment.regional_jet(), 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  def test_device_temperature(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

  def test_maximum_display_brightness(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)

unittest.main()

#Expected failures
#Expected failures are counted as passed in our test results. If the test passes when we expected it to fail, then it is marked as
#failed in test results

#expectedFailure decorator
class FeatureTests(unittest.TestCase):

    @unittest.expectedFailure #No args
    def test_broken_feature(self):
        raise Exception("This test is going to fail") #test will always fail because raised exception during test exec

#In the unittest module, which of the following skip functions is NOT a decorator?
    #A: skipTest