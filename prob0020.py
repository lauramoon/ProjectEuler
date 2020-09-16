"""
Project Euler Problem 20. https://projecteuler.net/problem=20
"""

import math

# calculate 100!
x = math.factorial(100)

# turn ut into a string
x = str(x)

# sum of the digits of x
total = 0

for char in x:
    total += int(char)

print(total)