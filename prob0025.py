"""
Project Euler Problem 25. https://projecteuler.net/problem=25
"""

import math


def fibonacci_gen():
    """Fibonacci generator"""
    previous = 0
    current = 1

    while True:
        yield current
        following = previous + current
        previous = current
        current = following


# Using the limit ratio of Fibonacci numbers to figure out when we get over 1000 digits
fibonacci = fibonacci_gen()
# The Golden ratio
base = (1 + 5**.5)/2
for i in range(1, 30):
    print(f"{i}: {next(fibonacci)} -- {round(base**(i-2)*1.17082, 0)}")

# The ith Fibonacci is the golden ratio raised to the (i-2) power, times a number slightly over 1.
adjustment = 1.17082**(1/999)
# This solves for i-2 when the fibonacci number is 10^999 (i.e., 1000 digits)
print(999*math.log(10/adjustment, base))




