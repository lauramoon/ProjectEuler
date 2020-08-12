"""
Project Euler Problem 2. https://projecteuler.net/problem=2
"""


def even_fib_sum(n):
    """
    Sums all even Fibonacci numbers up to a number n
    :param n: max value of Fibonacci number
    :return: integer sum of all lower even Fibonacci numbers.
    """
    # Start with first even Fibonacci
    total = 2

    # Current highest 3 numbers
    x1 = 1
    x2 = 2
    x3 = x1 + x2

    while x3 < n:
        # if even, add to total
        if x3 % 2 == 0:
            total += x3

        # reset current highest Fibonacci numbers
        x1, x2 = x2, x3

        # calculate next Fibonacci
        x3 = x1 + x2

    return total


print(even_fib_sum(4000000))

