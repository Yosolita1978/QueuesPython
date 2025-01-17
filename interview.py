# Generate a list of Binary  Numbers from 1 to N - please use a Queue
# Your function will take N as input and return a list of binary 
# numbers from 1 to N in the order they were generated.

from collections import deque

def generate_binary_numbers(n):
    """This function generates a list of binary numbers from 1 to N"""
    
    queue = deque()
    queue.append("1")
    binary_numbers = []
    for i in range(n):
        binary_numbers.append(queue.popleft())
        queue.append(binary_numbers[i] + "0")
        queue.append(binary_numbers[i] + "1")
    return binary_numbers

print(generate_binary_numbers(5))
# ['1', '10', '11', '100', '101']