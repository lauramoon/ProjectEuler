"""
Project Euler Problem 24
"""
import math


def find_permutation(n, digits):
    """
    If all permutations of the given number of digits are arranged in numerical order,
    returns the nth permutation
    :param n: which perutation to return
    :param digits: how many digits to permute (0 to digits-1)
    :return: the nth permutation as a string
    """
    # this algorithm counts from zero, so have to decrement n by 1
    n = n-1
    # list of the digits to be used in order
    digit_list = []

    # populate list
    for i in range(0, digits):
        digit_list.append(i)

    # list of digits in final order
    final_list = []
    # portion of n not yet accounted for
    chunk = n

    for i in range(digits-1, 0, -1):
        # get the index of the next digit
        next_index = chunk//math.factorial(i)
        # put the digit in the final list and remove it from the digit list
        final_list.append(digit_list.pop(next_index))
        # calculate the remaining chunk
        chunk = chunk%math.factorial(i)

    final_list.append(digit_list[0])
    print(final_list)


find_permutation(1000000, 10)