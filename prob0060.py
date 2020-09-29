"""
Project Euler Problem 60. https://projecteuler.net/problem=60
The primes in a prime pair set must all equal the same thing mod 3, with the exception of 3 itself.
So we keep track of prime pair sets is two lists, one for those mod 3 = 1 and the other for mod 3 = 2.

Note that this code takes quite a while to run once you get to the first prime above 100000. You can get the answer
without going past that, but to prove it's the answer, you have to check past there. I'm sure there are
optimizations, but I haven't figured them out yet.
"""


def prime_generator():
    """
    This is the sieve of Erosthenes, as implemented by David Eppstein, UC Irvine, 28 Feb 2002
    For the (much less efficient) method of calculating primes that I came up with myself,
    see my solution to problem 7
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


def pair(n1, n2):
    """
    Returns the two integers created by concatenating the two integers provided both ways
    :param n1: positive integer
    :param n2: positive integer
    :return: two integers n1n2 and n2n1
    """
    c1 = int(str(n1) + str(n2))
    c2 = int(str(n2) + str(n1))

    return c1, c2


def augment_prime_set(prime_set, set_maximum, new_maximum, generator):
    """
    adds additional primes to the reference set of primes until the maximum value is greater than
    the maximum value given
    :param prime_set: set of primes
    :param set_maximum: current maximum of prime_set
    :param new_maximum: integer, set needs to have all allowed values below it
    :param generator: the generator for the reference sets of primes
    :return: new maximum value for the set
    """
    next_prime = 0

    while next_prime < new_maximum:
        next_prime = next(generator)
        prime_set.add(next_prime)
        set_maximum = next_prime

    return set_maximum


def prime_pair_sets():
    """

    :return:
    """
    # initialize reference set of primes
    prime_set = {3}
    maximum = 3

    # initialize list of sets, one for mod 3 = 1 and one for mod 3 = 2
    set_list_1 = [{3}]
    set_list_2 = [{3}]

    # prime generators: one for adding to the reference set, one for the prime under consideration
    prime_gen_for_reference = prime_generator()
    prime_gen_for_checking = prime_generator()
    next_prime = 0

    # primes 2 and 5 don't work, and 3 included above, so run both prime generators to 7

    while next(prime_gen_for_reference) < 5:
        next(prime_gen_for_reference)

    while next(prime_gen_for_checking) < 5:
        next_prime = next(prime_gen_for_checking)

    while next_prime < 26000:
        next_prime = next(prime_gen_for_checking)

        # determine which set list to use
        if next_prime % 3 == 1:
            set_list = set_list_1
        else:
            set_list = set_list_2

        # set of primes that don't work with next_prime
        exclude_set = set()

        if next_prime >= 10007:
            print("Reached", next_prime)
            print("Sets to test:", len(set_list))
        # check sets
        for i in range(0, len(set_list)):
            # only check if potentially better than current best set of five primes
            length = len(set_list[i])
            if sum(set_list[i]) + next_prime*(5-length) > 26033:
                continue

            # initialize success in this checking to true
            success = True

            # check each item in set
            for item in set_list[i]:
                # can skip the rest if already determined that one number combo out
                if item in exclude_set:
                    success = False
                    break

            if not success:
                continue

            for item in set_list[i]:
                pair_a, pair_b = pair(next_prime, item)

                # augment sets if necessary
                if max(pair_a, pair_b) > maximum:
                    maximum = augment_prime_set(prime_set, maximum, max(pair_a, pair_b), prime_gen_for_reference)

                # if either pair not in prime set, no success
                if pair_a not in prime_set or pair_b not in prime_set:
                    success = False
                    exclude_set.add(item)
                    break

            if success:
                new_set = set_list[i].copy()
                new_set.add(next_prime)
                set_list.append(new_set)
                if len(new_set) == 5:
                    print("*******************************")
                if len(new_set) > 3:
                    print("New set:", new_set)
                if len(new_set) == 5:
                    print("*******************************")

        if next_prime < 5200:
            set_list.append({next_prime})


prime_pair_sets()