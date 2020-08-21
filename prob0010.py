"""
Project Euler Problem 10. https://projecteuler.net/problem=10
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


def prime_sum(max_value)->int:
    """
    Sums all prime numbers up to the specified value. Returns the sum.
    :param max_value: primes up to (and including, if prime) are added
    :return: the sum of primes up to max_value
    """
    prime_gen = prime_generator()
    current_prime = next(prime_gen)
    total = 0

    while current_prime < max_value:
        total += current_prime
        current_prime = next(prime_gen)

    return total

print(prime_sum(2000000))