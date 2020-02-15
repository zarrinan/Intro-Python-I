# Check if a number is prime

from math import sqrt
from itertools import count, islice

def isPrime(num):
    # Check if num is greater than 1
    if num < 2:
        return False
    # Within a range of numbers from 2 to int(sqrt(num) - 1) with step=+1,
    # check if num is divisible by any of them
    for number in islice(count(2), int(sqrt(num) - 1)):
        if n % number == 0:
            return False
    return True
