#Sequential Programming
"""
Programs that follow a set order of instructions from beginning to end
i.e.
"""
for i in range(4):
    print(i)
print('end')

"""
Let’s imagine we are a data scientist working on a complex learning model or a backend developer working with 
an extensive database. Suddenly, we are dealing with many more steps that take a lot more processing power.

In situations like this, the concepts of concurrent programming and parallel programming come into play. 
To give us a basic intuition behind each of these paradigms, let’s picture three separate scenarios of ordering food at a deli.
"""

#Analogy
"""
Imagine you are at a store with a lot of customers with 1 singular line/queue. This amount of customers would be a pain to process.
Opening multiple lines would be much more efficient in dealing with the queue. 

Concurrent programming can be viewed as multiple lines of customers with access to one register. 
Parallel programming can be viewed as multiple lines of customers with access to multiple registers that can divvy ip the customers

Asynchronous programs can be viewed as having a qait queue where each customer has a ticket. Once a customer's food is ready, 
their ticket gets called. However, the tickets don't necessarily get called in order; Instead, any ticket ca be called once the
customer's food is ready unlike sequential (synchronous).
"""

#Terms
"""
Concurrency: process in which we have multiple tasks running and completing during overlapping periods of time
Parallelism: the process in which we simultaneaously have multiple tasks or separate parts of the same task running
using multiple CPUs. 

What's the difference?
Parallelism requires multiple units of hardware while concurency utilizes one
Concurrency requires at least two tasks to exist while parallelism only requires one
Parallelism assigns each task for a core to execute whereas concurrency executes all tasks by switching tasks simultaneously
Parallelism can do multiple things at once while concurrency means we can juggle between tasks
"""

#methods in python
#Libraries
"""
threading (concurrency)
multiprocessing (parallelism)
asyncio (asynchronous)
"""

#Lifecycle of a process
"""
To best optimize the performance of processes as their priority changes or as they wait for access to a limited resource, processes are
put into one of five states.
"""