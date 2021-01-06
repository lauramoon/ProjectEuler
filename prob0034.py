"""
Project Euler Problem 34. https://projecteuler.net/problem=34
"""
import math


def factorial_sum(n):
    """
    Calculate the sum of the factorial of the digits of the integer provided
    param n: integer
    return: sum of digit factorials
    """
    total = 0
    for digit in str(n):
        total += math.factorial(int(digit))

    return total


def main():
    total = 0
    for i in range(10, 10000000):
        if i == factorial_sum(i):
            print(i)
            total += i
    print(total)


main()
