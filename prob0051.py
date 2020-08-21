"""Project Euler Problem 51. https://projecteuler.net/problem=51
Selected because it's the first one with difficulty over 5%.
Note: The solution below does not guarantee finding the lowest solution;
there could be a set where 9 is not one of the repeated digits;
there could be a set where there are 4 nines in the highest number
but only 3 of them are repeated. But the first solution found
turns out ot be the correct one, according to Project Euler"""


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


def get_prime_list(low, num):
    """
    assembles list of num consecutive primes starting with the one at or just above low
    Note: not used in solution - better to make set and grab primes from the generator as needed
    :param low:
    :param num:
    :return: list of primes
    """
    prime_gen = prime_generator()
    current_prime = 2

    while current_prime < low:
        current_prime = next(prime_gen)

    result = [current_prime]
    for i in range(num):
        result.append(next(prime_gen))

    return result

def check_for_replacements(prime, digit, prime_set):
    """
    replaces the 3 given digits in given prime with lower digits,
    checks if each of the resulting numbers is in prime set
    :param prime: prime number with 3 identical digits
    :param digit: digit to replace
    :param prime_set: set of primes up to the given prime
    :return: list of primes meeting criteria
    """
    # result includes the prime provided
    prime_list = [prime]
    # turn it into a string
    prime_string = str(prime)
    # consider each digit up to the given one
    for i in range(0, digit):
        # replace identified digit with i (using string methods)
        replaced = prime_string.replace(str(digit), str(i))
        # check if integer form is prime
        if int(replaced) in prime_set:
            # if it's prime, add to list of results
            prime_list.append(int(replaced))

    return prime_list


def digit_replacement():
    """
    checks list of primes to find set of 8 primes that differ only by a subset of the digits
    and where that subset is the same in each number but eight different digits across the list.
    (eg., *3 represents 6 different primes - 13, 23, 43, 53, 73, and 83; this function looks for 8)
    :return: list of 8 primes meeting criteria
    """
    # the lowest that works for a list of 7 is 56003, so presumably 8 is higher
    # create set of up to 1,000,000 primes, starting with 56003.
    prime_set = {56003}
    prime_gen = prime_generator()

    # start with lowest prime
    current_prime = 2

    # skip primes up to a little below 56003
    while current_prime < 55000:
        current_prime = next(prime_gen)

    # check each new prime with three 9's (can't have set of 8 with fewer)
    for i in range(1000000):
        # get next prime
        current_prime = next(prime_gen)
        # add it to set of primes
        prime_set.add(current_prime)
        # make it into a string
        string_prime = str(current_prime)

        # count of 9's
        count = 0
        # count the 9's
        for char in string_prime:
            if char == "9":
                count += 1
        # if there are 3, look for primes replacing the 9's
        if count == 3:
            prime_list = check_for_replacements(current_prime, 9, prime_set)
            if len(prime_list) > 7:
                return prime_list


print(digit_replacement())





