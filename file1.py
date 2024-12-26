"""
This module provides functions for working with prime numbers.

Functions:
- is_prime(n: int) -> bool: Checks if a number is a prime number.
- find_primes_up_to(limit: int) -> list[int]: Finds all prime numbers up to a specified limit.
- list_primes_in_range(start: int, end: int) -> list[int]: Lists all prime numbers within a given range.

The script also includes an example usage in the `__main__` block to demonstrate functionality.
"""

import math
number = int(input("Enter a number to check if it's prime: "))
def is_prime(n: int) -> bool:
    """
    Find all prime numbers up to a given limit.

    Args:
        limit (int): The upper limit for prime numbers.

    Returns:
        list[int]: A list of prime numbers up to the given limit.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def find_primes_up_to(limit: int) -> list[int]:
    """
    Find all prime numbers up to a given limit.

    Args:
        limit (int): The upper limit for prime numbers.

    Returns:
        list: A list of prime numbers up to the limit.
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
def list_primes_in_range(start: int, end: int) -> list[int]:
    """
    List all prime numbers in a given range.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        list: A list of prime numbers in the range.
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
try:
    divisor = int(input("Enter a divisor for calculation: "))
    result = 100 / divisor
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
unused_variable = "This is not used anywhere"

#new line at the end of the file
