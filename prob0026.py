from decimal import *


def find_max_cycle():
    """
    checks all 1/d for integer d up to 999, getting the length of the shortest decimal cycle for 1/d.
    Returns the maximum shortest cycle length and it's associated integer.
    :return: tuple of the max cycle length and the integer that has that length
    """
    # maximum cycle length found so far, and its integer
    maximum = 0
    decimal = 1

    for i in range(1, 1000):
        cycle = get_cycle_length(i)
        if cycle > maximum:
            maximum = cycle
            decimal = i

    return maximum, decimal


def get_cycle_length(n):
    """
    checks integer n for the decimal cycle length of 1/n
    :param n: positive integer
    :return: cycle length (0 if decimal terminates)
    """
    # start with only 105 digits to get short cycles
    dec_str = get_decimal_string(n, 105)
    if len(dec_str) < 100:
        return 0

    check_100 = check_for_cycle(dec_str, 30)

    if check_100 != -1:
        return check_100

    dec_str = get_decimal_string(n, 1000)
    check_1000 = check_for_cycle(dec_str, 300)

    if check_1000 != -1:
        return check_1000

    dec_str = get_decimal_string(n, 10000)
    check_10000 = check_for_cycle(dec_str, 3000)

    if check_10000 != -1:
        return check_10000

    print("No cycle found up to 3000 digits")


def check_for_cycle(dec_str, max_check):
    """
    check for cycles in the decimal of 1/n up to max_check long
    :param n: integer
    :param max_cycle: maximum length to check
    :return: length of cycle; -1 if none found
    """

    for j in range(1, max_check):
        # skip first 10 chars, look for 3 cycles
        if dec_str[10:10 + j] == dec_str[10 + j:10 + 2 * j] == dec_str[10 + 2 * j:10 + 3 * j]:
            return j
    return -1


def get_decimal_string(d, length):
    getcontext().prec = length
    return str(Decimal(1) / Decimal(d))


print(find_max_cycle())
