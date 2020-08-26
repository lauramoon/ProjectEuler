"""Project Euler Problem 12. https://projecteuler.net/problem=12"""


def triangular_gen():
    """
    Generates triangular numbers (sum of consecutive positive integers up to a number)
    NOTE: unneeded as triangular numbers can be calculated directly
    yield: next triangular number
    """
    n = 1
    next_num = n
    while True:
        yield next_num
        n += 1
        next_num += n


def count_divisors(n):
    """
    counts the number of divisors for the given number
    NOTE: this brute-force method takes too long, method with dictionary below
    :param n: positive integer
    :return: number of divisors
    """

    # initialize with one for the number itself
    count = 1
    # only need to go up to half n since already counted n
    for i in range(1, int(n/2 + 1)):
        if n % i == 0:
            count += 1

    return count


def add_to_divisor_map(n, div_map):
    """
    adds n to divisor map with n as the key and its set of divisors as the value
    :param n: positive integer
    :param div_map: map divisors of all lower integers
    """
    # start with trivial divisors
    div_map[n] = {1, n}

    # look for lowest divisor above 1, will be prime
    for i in range(2, n):
        if n % i == 0:
            # call this first divisor prime
            prime = i

            # add to n's divisors in map
            div_map[n].add(prime)
            # and add in case it's not there
            div_map[i] = {1, prime}

            # add the other divisor to map if not there
            other = n // i
            if other not in div_map:
                add_to_divisor_map(other, div_map)

            # update map with additional divisors for n from other
            div_map[n] = div_map[n].union(div_map[other])

            # update map with prime divisor times each of other's divisors
            for divisor in div_map[other]:
                div_map[n].add(prime * divisor)

            # all divisors of n should be there, so break
            break


def count_divisors_triangular_number(n):
    """
    looks for first instance of a triangular number having greater than n divisors
    :return: first instance
    """
    # divisor map has integer as key and all of its divisors as a set as the value
    # initialize with the first three positive integers
    divisor_map = {1: {1}, 2: {1, 2}, 3: {1, 3}}

    # check out ith triangular number
    for i in range(2, 20000):
        # calculate ith triangular number
        tri_num = int(i * (i + 1) / 2)

        # get divisors of current triangular number
        add_to_divisor_map(tri_num, divisor_map)
        divs = len(divisor_map[tri_num])

        # checking on progress
        if divs > 250:
            print(i, tri_num, divs)

        # return triangular number if number of divisors is high enough
        if divs > n:
            return tri_num
