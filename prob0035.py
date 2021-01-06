"""
Project Euler Problem 35: Circular Primes https://projecteuler.net/problem=35
"""


def prime_generator():
    """
    This is the sieve of Erosthenes, as implemented by David Eppstein, UC Irvine, 28 Feb 2002
    For the method of calculating primes that I came up with myself, see my solution to problem 7
    :return: the next prime number
    """
    # map of composites (key) with at least one prime factor in list as value
    D = {}

    # first number to test if prime
    q = 2

    while 1:
        if q not in D:
            # next prime found
            yield q
            # add it's square as a composite to D
            D[q**2] = [q]
        else:
            # update dictionary entries based on composite and its listed primes
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1


def get_candidates(n):
    """
    Checks digits of prime numbers up to n, puts in candidate set if only contains
    1, 3, 7, and/or 9.
    return: set of integers
    """
    # set of primes that might be circular
    candidates = {11}
    prime_gen = prime_generator()
    # skip first 4 primes
    for i in range(0, 4):
        current = next(prime_gen)

    # loop through all primes up to n
    while current < n:
        current = next(prime_gen)
        possible = True

        # check each digit of current prime
        for digit in str(current):
            if digit not in ['1', '3', '7', '9']:
                possible = False

        if possible:
            candidates.add(current)

    return candidates


def get_rotations(n):
    """
    creates set of rotations for number. E.g., 197 returns {197, 971, 719}
    param n: integer for which to get rotations
    return: set of integers with rotated digits
    """
    # need to add len(n) - 1 integers to set
    rotations = {n}
    for i in range(len(str(n)) - 1):
        string = str(n)[i + 1 :] + str(n)[: i + 1]
        rotations.add(int(string))
    return rotations


def main():
    # set of circular primes
    circulars = {2, 3, 5, 7}
    candidates = get_candidates(100)

    while len(candidates) > 0:

        # get number from set
        candidate = candidates.pop()

        # get set of rotations for the candidate
        rotations = get_rotations(candidate)
        circular = True

        # check if each number is in the candidate set of primes
        for number in rotations:
            if number not in candidates and number != candidate:
                circular = False

        if not circular:
            continue

        # if it is circular, add all in set to circulars and delete from candidates
        for number in rotations:
            circulars.add(number)
            candidates.discard(number)

    return circulars

