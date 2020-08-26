"""
Project Euler Problem 16. https://projecteuler.net/problem=16
This one is rather trivial in python with no maximum integer
to be concerned with.
"""

product = 2**1000

string = str(product)
total = 0

for char in string:
    total += int(char)

print(total)
