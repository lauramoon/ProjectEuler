"""Euler Project Problem 7. https://projecteuler.net/problem=7"""

def get_nth_prime(n):
    """
    Finds the nth prime number (2 is first, 3 is second, etc)
    :param n: positive integer
    :return: nth prime number
    """
    # initialize list of primes
    prime_list = []

    # starting number to check
    x = 2

    # consider all integers until n primes are found
    while len(prime_list) < n:

        # track if factor found for x
        factor_found = False
        for i in prime_list:
            # if no factors up to root x, x is prime
            if i > x**.5:
                break
            # if i is a factor, x is not prime
            if x % i == 0:
                # if factor found, change bool, escape from loop
                factor_found = True
                break

        # if no factor found, append x to list of primes
        if not factor_found:
            prime_list.append(x)

        x += 1

    # once prime list has n items, return the last item
    return prime_list[-1]


print(get_nth_prime(10001))

