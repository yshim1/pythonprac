#Three modules
" threading, asynio, multiprocessing "
import time
def sequential():
  s = time.perf_counter() #performance counter that returns float time in seconds
  print("Codecademy")
  time.sleep(2) #delay of 2 seconds in execution of program
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

sequential()


#Threading module
#in python, threads do not actually run simultaneusly, they only appear to do so
import threading
"""
example_thread = threading.Thread(target=some_function, args=(some_arg,))

target: this is the function you want to execute with thread(s). Defaults to None
args: this is the argument or set of arguments applied to the target function/ It is a tuple that defaults to None

thread is started to make sure it executes on Run
threadName.start
"""

import time
import threading
def greeting_with_sleep(string):
  s = time.perf_counter()
  print(string)
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")


greeting_with_sleep('Codecademy')

t = threading.Thread(target=greeting_with_sleep, args=('Codecademy',)) #Notice how 'Codecademy' must have a comma to signify it is a tuple
t.start()
"""
Note that the time is essentially the same because it one task and one thread. There is no way to speed up the task
"""

#Using Multiple Threads
#Two ways to use multithreading
"""
# create each thread
t1 = threading.Thread(target=target_function, args=(arg1,))
t2 = threading.Thread(target=target_function, args=(arg2,))
t3 = threading.Thread(target=target_function, args=(arg3,))
# start each thread
t1.start()
t2.start()
t3.start()
"""
#Preferred method
"""
threads = []
# list of arguments to use
args = [arg1, arg2, arg3]
# iterate through the length of arguments
for i in range(len(args)):
  # create thread
  t = threading.Thread(target=target_function, args=(args[i],))
  # add thread to threads list
  threads.append(t)
  # start thread
  t.start()
"""
import time
import threading
def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print("says hello!")


def main_threading():
  s = time.perf_counter()
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  # your code goes here
  for i in range(len(greetings)):
    t = threading.Thread(target=greeting_with_sleep, args=(greetings[i],))
    t.start()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

main_threading()
"""
OUTPUT:
Codecademy
Chelsea
Hisham
Ashley
Threading Elapsed Time: 0.0006165840022731572 seconds
says hello!
says hello!
says hello!
says hello!

Why did the elapsed time come before the say hello come later in the output? This is because each thread has started but python
is waiting for the last thread to finish before terminating. Therefore, while mainthreading has completed, greeting_with_sleep
is still executing in the final thread
"""

#Joining a thread
"""
We can use join to tell one thread to wait for this thread to stop before moving on
"""
import time
import threading
def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print("says hello!")


def main_threading():
  s = time.perf_counter()
  threads = []
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  for i in range(len(greetings)):
    t = threading.Thread    (target=greeting_with_sleep, args=(greetings[i],)) 
    t.start()
    # add append code here
    threads.append(t)
  # add join code here
  for thread in threads:
    thread.join()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

main_threading()
"""
After using join, mainthreading does not complete until each thread has been executed
OUTPUT: 
Codecademy
Chelsea
Hisham
Ashley
says hello!
says hello!
says hello!
says hello!
Threading Elapsed Time: 2.002659363002749 seconds

If we were to do sequential, we would get because we would run into time.sleep(2) four times
Codecademy
says hello!
Chelsea
says hello!
Hisham
says hello!
Ashley
says hello!
Threading Elapsed Time: 8.008541757997591 seconds

Also, why is the output order the names then the greeting? This is because when each thread is blocked by time.sleep(2), 
they begin to work concurrently to complete each task
"""

#Asyncio
"""
async kw declares a function as a coroutine. Coroutines are functions that may return normally with a value or may suspend
themselves internally and return a continuation. Basically, they allow tasks to be paused and resumed to mimic multitasking

await: suspends execution of the current task until whatever is being 'await'ed on is completed
ie 'await function task2' within a coroutine 'task1' means suspend task 1 until task 2 is completed
"""
import asyncio
async def hello_async():
  print("hello")
  await asyncio.sleep(3)
  print("how are you?")

#Old syntax to run the coroutine
"""
loop = asyncio.get_event_loop()
loop.run_until_complete(hello_async())
"""
#Current syntax (as of 3.7)
asyncio.run(hello_async)

import time
import asyncio

async def greeting_with_sleep_async(string):
  s = time.perf_counter()
  print(string)
  await asyncio.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

loop = asyncio.get_event_loop()
loop.run_until_complete(greeting_with_sleep_async('Codecademy'))

#Multiple Asynchronous Tasks
#Similar setup to multiple threads
"""
async def main():
  tasks = [task1(arg1), task2(arg2), task3(arg3)]
  await asyncio.gather(*tasks) 
"""

"""
Here, we define main as a corouting function. tasks is a list of separate function calls. Note that each of task1(), task2(), and
task3 are coroutine functions.

"""