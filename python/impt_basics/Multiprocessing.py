# Multiprocessing
# Involves running multiple processes, each with its own memory space
# Use for CPU-bound tasks: Tasks that require a lot of computation, such as mathematical calculations, image processing, etc.

import multiprocessing
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in "abcde":
        time.sleep(1.5)
        print(letter)

if __name__ == "__main__":
    # Create processes
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    print("Both processes have finished!")
