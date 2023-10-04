#Sequential Programming
"""
Programs that follow a set order of instructions from beginning to end
i.e.
"""
for i in range(4):
    print(i)
print('end')

"""
Lets imagine we are a data scientist working on a complex learning model or a backend developer working with 
an extensive database. Suddenly, we are dealing with many more steps that take a lot more processing power.

In situations like this, the concepts of concurrent programming and parallel programming come into play. 
To give us a basic intuition behind each of these paradigms, lets picture three separate scenarios of ordering food at a deli.
"""

#Analogy
"""
Imagine you are at a store with a lot of customers with 1 singular line/queue. This amount of customers would be a pain to process.
How can you solve this issue?

Concurrent programming can be viewed as multiple lines of customers with access to one register. 
Parallel programming can be viewed as multiple lines of customers with access to multiple registers that can divvy ip the customers

Asynchronous programs can be viewed as having a wait queue where each customer has a ticket. Once a customer's food is ready, 
their ticket gets called. However, the tickets don't necessarily get called in order; Instead, any ticket can be called once the
customer's food is ready unlike sequential (synchronous).
"""

#Terms
"""
Concurrency: process in which we have multiple tasks running and completing during overlapping periods of time
Imagine a chef (processing resource) that chops salad while occasionally stirring soup. The chef will have to stop one task to do the other
and repeat this process until everything is done.

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

#Intro to processes
"""
Whie a computer program is a static collection of coded instructions stored on a disk, a process is an abstraction representing
the program while running. A process is made when a program is executed. The OS is responsible for managing these processes

The key defining factor is that processes generally operate independently and do not share data
"""

#Lifecycle of a process
"""
To best optimize the performance of precesses as their priority changes or as they wait for access to a limited resource (such as computing),
they are put into 1 of 5 states

New: The program has been started and waits to be added into memory in order to become a full process
Ready: Process fully initialized, loaded into memory, and waiting to be picked up by the processor
Running: Currently being executed by the processor
Blocked: The process requires a contested resource that it must wait for
Finished: The process has been completed

Blocking isn;t inherently negative. Some process may also be reverted to the ready state through preemption, where tasks are temporarily
interrupted by an external scheduler for urgent reasons, such as hardware interrupt signal asking the system to shutdown

All of these switching processes do come with overhead that is best to be avoided. This is called context switching and is typically
an expensive operation as the current state of the prcess needs to be stored and then be reloaded later to resume execution

New -> Ready -> <- Running -> Finished
        <- Blocked <-
"""

#Process Layout and Process Control Block
"""
When a process is initialized, its layout within memory has four distinct sections
(1-5) in sequential order from start of memory address to end of memory address
1. text section for compiled code 
2. data section for initialized variables
3. heap for dynamic memory allocation
4. Unallocated Memory
5. Stack for function variables

Processes are also initialized with process control block that is required by the operating system for managing the process
This contains:

-A unique process ID and the ID of any parent processes that launched the current one
-The current process state
-How long the process has been running and any time limits the process may have
-Allowed system resources and other permissions
-The priority of the process
-The program counter for the address of the instruction currently being executed
-The address of other registers within the CPU holding intermediate values
-Information required for memory management such as page and segment tables

When one process launches another, the original enters a parent-child relationship that shares much of the above data
ie: music player that starts a new process that will allow toggling of external speakers

Parent processes wait for children to complete before terminating themselves unless child was created specifically to run independently
in the background
"""

#Intro to Threads
"""
A process is an abstract data structure representing info to run a program. A thread represents the actual sequence
of processor instructions that are actively being executed

Each process needs at least 1 thread to be able to execute although more can be created to allow for concurrent processing
Threads live within the processes and share al the common resources available to it like memory pages and active files

These shared resources are critical for definition of a thread. While each process is typically independent, multiple threads
usually work together within the context of a process. By sharing data directly, there is faster communication and context switching
between threads than what is possible for all processes while taking fewer system resources.

i.e.
Within a video game process, multiple threads may exist to manage separte services such as collecting user input and producing sound.
As these threads live within the same process, they can share information about the game, such as the type of ground the player
is walking on. This can be used to affect both the speed the character moves from the input thread asa well as the noises created 
in the sound thread
"""

#Multithreading
"""
Typically, a single CPU core can only execute 1 thread so 1 preocess at time. With use of blocking and context switching
this limitation can be obscured to users through nanosecond-long pauses that allow proccesses to be completed near-simultaneously
thus allowing single CPU cores to execute multiple threads at once aka multithreading

Parallelizing has benefits such as improved system utilization and system responsiveness because tasks can be evenly split among
multiple threads exhausting all available computing resources and allowing longer tasks to run in background, independent of user
input
Cons:
programs are more difficult to write due to nonsynchronous nature and new types of bugs

2 of the most common examples are data races, where multiple threads attempt to modify the same piece of data, and 
deadlocks where multiple threads all attempt to wait for each other and freeze the system

Since these bugs are related to tight timing of CPU interactions, the programs can be considered non-deterministic and therefore
untestable
"""

#Kernel Threads vs User Threads
"""
A thread built into an existing process is considered a kernel thread. this means that the kernel(main part of OS that facilitates
interaction between hw and sw) is fully aware of these threads and directly manages their execution

There are also user threads that exist solely in userspace and while functionally identical, are not known or controlled
by the kernel. This allows for more fine-grained control by devs. These threads are more effecient than their kernel
counterparts as they save on the costly indirection of making a system call to constantly interact with the kernel

Although they operate independently of the kernel, they do need to be mapped to existing kernel threads in order to have
the operating system execute them. There are 3 common models for mapping user to kernal threads

1:1 kernel-level threading: for simple implementation that best allows for hardware acceleration provided by the kernel threads

N:1 User-level threading: for ultra light threads that can quickly communitcate and context switch, but do not benefit from hardware
acceleration due to sharing the same kernel thread

M:N Hybrid threading: to get the best of both above solutions: v light and fast that can be hw accelerated if need be. This complex
implementation can lead to bugs such as priority inversion where less important tasks are mistakenly priotized and run first


Hardware acceleration refers to the process by which an application will ofload certain computing tasks onto specialized
hardware components within the system, enabling greater efficiency thatn is possible in software running on a general-purpose CPU

Kernel threads are constructed through system calls to the kernel while user threads are constructed using local function calls
"""

#When is a process blocked?
"""
When the process has to wait for a contested, limited, or slow resource, such as accessing a specific file, or waiting for a network
request
"""