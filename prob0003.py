""" Project Euler Problem 3. https://projecteuler.net/problem=3"""
import math


def is_factor(factors: list, num: int) -> bool:
    """
    tests whether any numbers in the list 'factors' are factors
    of the integer 'num'. Returns True if any number in the list
    is a factor of num.
    :param factors: list of integers
    :param num: number being checked for factors
    :return: True if any numbers are factors, False otherwise
    """
    for x in factors:
        if num % x == 0:
            return True

    return False


def dupli_factors(factor: int, num: int) -> int:
    """
    returns the numbers of times a number is a factor of another number.
    :param factor: integer, the factor being tested (ideally prime)
    :param num: number being tested for factors
    :return: integer number of times factor divides evenly into num
    """
    times = 0
    test = num
    while factor <= test:
        if test % factor == 0:
            times += 1
            test = test/factor
        else:
            break

    return times


def greatest_factor(num: int) -> int:
    """
    Returns the greatest prime factor of the integer 'num'.
    If num is negative, 0, or 1, returns 1
    if prime, returns the number
    :param num: integer
    :return: integer, highest factor of num
    """
    if num <= 1:
        return 1

    # factors found
    factors = []
    # primes, will add to list below
    primes = [2]

    # test 2 as factor, find how many times, add to list of factors
    num2 = dupli_factors(2, num)
    factors += [2]*num2

    if math.prod(factors) == num:
        return 2

    # one more special case:
    if num == 3:
        return 3

    # find next prime using latest list of primes, check if factor
    x = 3
    while x <= num:
        # nothing happens unless x is prime
        if not is_factor(primes, x):
            primes.append(x)

            # find how many times x is factor, add to list of factors
            numx = dupli_factors(x, num)
            factors += [x]*numx

            # check if all factors found
            if math.prod(factors) == num:
                return x

            # Check if unfactored portion of num is less than square of x
            # if so, the unfactored portion must be the highest prime factor
            if math.prod(factors):
                # If at least one factor has been found, find unfactored portion
                unfactored = int(num/math.prod(factors))
            else:
                # If no factors have been found, the unfactored portion is the number
                unfactored = num

            if unfactored < x**2:
                return unfactored

        x += 1


print(greatest_factor(600851475143))
