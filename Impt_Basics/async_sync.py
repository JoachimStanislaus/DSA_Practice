# Synchronous Programming
# In a synchronous program, tasks are executed one at a time in a sequential manner.
# Each task must complete before the next one begins. If a task takes a long time, it blocks the entire program until it finishes.

import time

def task_1():
    print("Starting task 1...")
    time.sleep(3)  # Simulating a long-running task
    print("Task 1 completed!")

def task_2():
    print("Starting task 2...")
    time.sleep(2)  # Simulating a long-running task
    print("Task 2 completed!")

# Synchronous execution
task_1()
task_2()

# Asynchronous Programming
# In asynchronous programming, tasks can start running without waiting for other tasks to complete.
# While one task is waiting (e.g., for I/O), other tasks can continue execution.
# This is typically implemented using coroutines, and in Python, it’s done with async and await.

# Limitations of Asynchronous Programming
# Complexity: Async code can be harder to debug and understand compared to sync code.
# CPU-Bound Tasks: Async is not suitable for tasks that require heavy computation, as it doesn’t leverage multiple CPU cores. For CPU-bound tasks, use multiprocessing or multithreading.
# Compatibility: Libraries must support async natively for it to be effective (e.g., async-compatible database or HTTP libraries).

import asyncio

async def task_1():
    print("Starting task 1...")
    await asyncio.sleep(2)
    print("Task 1 completed!")
    return "Result from task 1"

async def task_2():
    print("Starting task 2...")
    await asyncio.sleep(1)
    print("Task 2 completed!")
    return "Result from task 2"

async def main():
    # Run both tasks concurrently and wait for them to complete 
    # Use asyncio.gather() when you need to run several asynchronous operations at the same time and collect their results.
    # If any coroutine raises an exception, asyncio.gather() raises the first exception encountered, and subsequent tasks may or may not complete.
    results = await asyncio.gather(task_1(), task_2()) # The results are returned in the same order as the coroutines were passed to asyncio.gather(), regardless of the order in which they complete.
    print(results)

asyncio.run(main())

# Using asyncio.create_task() instead of asyncio.gather()
# Creates individual tasks for the coroutines task_1, task_2, and task_3.
# These tasks are scheduled to run concurrently.
# You can await tasks in an arbitrary order based on your program's logic. This lets you control which tasks' results you need first, while the other tasks continue running in the background.

import asyncio

async def task_1():
    print("Task 1: Starting...")
    await asyncio.sleep(3)  # Simulating a long-running task
    print("Task 1: Completed!")
    return "Result from task 1"

async def task_2():
    print("Task 2: Starting...")
    await asyncio.sleep(2)  # Simulating a shorter task
    print("Task 2: Completed!")
    return "Result from task 2"

async def task_3():
    print("Task 3: Starting...")
    await asyncio.sleep(1)  # Simulating the shortest task
    print("Task 3: Completed!")
    return "Result from task 3"

async def main():
    # Create tasks to run concurrently
    t1 = asyncio.create_task(task_1())
    t2 = asyncio.create_task(task_2())
    t3 = asyncio.create_task(task_3())

    # Wait for tasks to complete and get their results
    result_1 = await t1
    result_2 = await t2
    result_3 = await t3

    print("\nAll tasks completed!")
    print(result_1)
    print(result_2)
    print(result_3)

# Run the main function
asyncio.run(main())



