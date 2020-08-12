"""
Project Euler problem 1. https://projecteuler.net/problem=1
"""


def sum_mult_3_and_5(n):
    """
    This functions provides the sum of all multiples of 3 and 5
    up to (but not including) an integer n
    :param n: positive integer
    :return: sum of multiples of 3 and 5 less than n
    """
    total = 0
    for x in range(0, n):
        if x % 3 == 0 or x % 5 == 0:
            total += x

    return total


print(sum_mult_3_and_5(1000))
