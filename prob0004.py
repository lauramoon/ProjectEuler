"""Project Euler Problem 4. https://projecteuler.net/problem=4"""


def palindrome_3d():
    """
    produces a set of all 3-digit palindromic numbers
    Note: unused in solution; as problem misread at first
    (If the factors must also be palindromes, answer is 666,666)
    :return: set of 90 3-digit integers
    """
    p3d = set()
    for i in range(100, 1000):
        if i // 100 == i % 10:
            p3d.add(i)

    return p3d


def palindrome_6d_gen():
    """
    generates the next 6-digit palindromic number, starting with the highest product of two 3-digit
    numbers (998,001), down to the lowest (100,001).
    Note problem does not exclude lower solutions, but one is found in this range
    :yield: next 6-digit palindromic number
    """
    for i in range(998001, 100000, -1):
        # turn number into a string
        s = str(i)
        if s[0] == s[5] and s[1] == s[4] and s[3] == s[2]:
            yield i


def check_for_factors():
    """
    checks each 6-digit palindromic number for 3-digit factors
    :return: highest 6-digit palindrome equal to product of two 3-digit palindromes
    """
    factors = palindrome_3d()

    for i in palindrome_6d_gen():
        for j in range(100, 1000):
            if i % j == 0 and int(i/j) < 1000:
                return i, j


solution = check_for_factors()
print(solution)

