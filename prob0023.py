"""
Project Euler Problem 23. https://projecteuler.net/problem=23
"""


def is_abundant(num):
    """
    Determines if the sum of the integer's proper divisors is greater than the integer
    :param num: positive integer
    :return: true if the sum of proper divisors is greater than num; false otherwise
    """

    # set of all proper divisors
    divisors = {1}

    # consider all integers from 2 thru the square root of num
    for i in range(2, int(num**.5)+1):
        # if i divides evenly
        if num % i == 0:
            # put both and and the other divisor in the set of divisors
            divisors.add(i)
            divisors.add(num//i)

    # if the sum is greater than num, return true
    if sum(divisors) > num:
        return True
    else:
        return False


def is_abundant_sum(num, abundant_set):
    """
    determines if num is the sum of two abundant numbers
    :param num: positive integer
    :param abundant_set: set of abundant numbers up to 28123
    :return: true if there are two abundant numbers that sum to num; false otherwise
    """
    # as 12 is the lowest abundant number, start there, go thru half of num
    for i in range(12, num//2+1):
        # if i and num - i are in the set of abundant numbers, return true
        if i in abundant_set and num-i in abundant_set:
            return True
    # if no pair of abundant numbers sums to num, return false
    return False


def main():
    """
    get set of abundant numbers up to 28123 (all non-abundant sums are less than this),
    identify integers that aren't a sum of those such numbers, sum these numbers
    """
    abundant_set = {12}

    for i in range(14, 28123):
        if is_abundant(i):
            abundant_set.add(i)

    non_abundant_sums = []

    for i in range(1, 28123):
        if not is_abundant_sum(i, abundant_set):
            non_abundant_sums.append(i)
            
    print(sum(non_abundant_sums))

main()