"""
Project Euler Problem 27: Quadratic Primes https://projecteuler.net/problem=27
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
            # add its square as a composite to D
            D[q**2] = [q]
        else:
            # update dictionary entries based on composite and its listed primes
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1


def get_length(a, b, prime_set):
    """
    calculates how many consecutive primes n^2 + an + b produces,
    starting at n = 0, returns the number
    :param a: the coefficient of n
    :param b: the lone integer
    :param prime_set: the et of primes calculated earlier
    :return: number of consecutive primes produces by the formula
    """
    consecutive = 0
    n = 0
    while n < 100:
        if n*n + a*n + b in prime_set:
            consecutive += 1
        else:
            break
        n += 1

    return consecutive


def find_coefficients(n):
    prime_gen = prime_generator()
    prime_set = {2}
    for i in range(500000):
        prime_set.add(next(prime_gen))

    for a in range(0, n):
        for b in range(0, n):
            prime_length = get_length(a, b, prime_set)
            if prime_length > 60:
                print(f"n^2 + {a}n + {b} has {prime_length} consecutive primes")
            prime_length = get_length(-a, b, prime_set)
            if prime_length > 60:
                print(f"n^2 -{a}n + {b} has {prime_length} consecutive primes")


find_coefficients(1000)
