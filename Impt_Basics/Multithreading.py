# Multithreading 
# Involves running multiple threads within a single process, share memory space and data.
# Lightweight, can switch between tasks without overhead of creating new processes.
# Use it for: I/O-bound tasks: Things like network operations, file reading/writing, database queries, etc., where the program spends most of its time waiting for external resources.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in "abcde":
        time.sleep(1.5)
        print(letter)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print("Both threads have finished!")

# Possible Race condition 
# A race condition occurs when two or more threads (or processes) try to access and modify shared data concurrently, and the final outcome depends on the order in which the threads execute. This can lead to unexpected or incorrect behavior in a program because the threads are not synchronized.

# Example: If two threads try to increment a shared variable at the same time, the final value might not be what you expect.

# Can resolve with thread locking to ensure only one thread can access the shared resource at one time.
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = []

# Create 2 threads
for _ in range(2):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

# Wait for both threads to finish
for t in threads:
    t.join()

print("Final counter value:", counter)  # Output: 200000


# Deadlock
# A deadlock is a situation where two or more threads (or processes) are blocked forever, waiting for each other to release resources that they need. This happens when the threads form a circular dependency, where each thread holds a resource and waits for another to release a resource that the other thread is holding.

# Example: Thread A holds Lock 1 and waits for Lock 2, while Thread B holds Lock 2 and waits for Lock 1. Both threads are stuck, unable to proceed.

import threading

# Two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_a():
    lock1.acquire()  # Thread A acquires Lock 1
    print("Thread A acquired Lock 1")
    threading.Event().wait(1)  # Simulate some work
    lock2.acquire()  # Thread A tries to acquire Lock 2, but it's held by Thread B
    print("Thread A acquired Lock 2")

def thread_b():
    lock2.acquire()  # Thread B acquires Lock 2
    print("Thread B acquired Lock 2")
    threading.Event().wait(1)  # Simulate some work
    lock1.acquire()  # Thread B tries to acquire Lock 1, but it's held by Thread A
    print("Thread B acquired Lock 1")

# Create and start threads
t1 = threading.Thread(target=thread_a)
t2 = threading.Thread(target=thread_b)

t1.start()
t2.start()

t1.join()
t2.join()

# To resolve, use timeouts so threads don't wait indefinitely or make sure you order them(lock acquisition) in the same order.
