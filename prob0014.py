"""
Project Euler Problem 14. https://projecteuler.net/problem=14 Collatz Sequence
"""


def find_next(num):
    """
    Finds next integer in Collatz sequence, where the next integer after n is
    n/2 if n is even, and 3n+1 if n is odd
    :param num:
    :return:
    """
    if num % 2 == 0:
        return int(num/2)
    else:
        return 3*num +1


def find_length(num):
    """
    takes number and finds the length of its Collatz sequence
    this is brute-force method, calculation for 1000000 integers is long; a generator is better
    :param num: positive integer
    :return: integer length of sequence
    """
    # initialize length at 1 (the number given)
    length = 1
    # initialize the current number as the one given
    current = num

    while True:
        if current == 1:
            return length
        else:
            current = find_next(current)
            length += 1


def gen_length(num):
    """
    generates the length of the Collatz sequence for integers from 3 to num
    uses dictionary to avoid repeat calculations
    :param num: max number to find length for
    :return: length of Collatz sequence for next integer
    """
    # initialize dictionary
    seq_map = {2: 2}

    # get all lengths starting at 3 up to num
    for i in range(3, num):
        # initialize current at i
        current = i
        # initialize length at 0
        length = 0

        # find the sequence, checking if the current number is in the dictionary
        while True:
            # if it gets to 1, found the length
            if current == 1:
                # update dictionary, yield the length, and go to next i
                seq_map[i] = length
                yield length
                break
            # if current is in dictionary, can look up the remaining length
            elif current in seq_map:
                # find final length
                length += seq_map[current]
                # add i to dictionary, yield length and go to next i
                seq_map[i] = length
                yield length
                break
            # otherwise, increment length and calculate next number in sequence
            else:
                length += 1
                current = find_next(current)


def find_longest(maximum):
    """
    checks for the number with the longest Collatz sequence in the range
    from 2 to the maximum number given
    :param maximum: maximum integer to check, must be positive integer
    :return: number with longest length and that length
    """
    # initialize number with longest chain at 2
    longest = 2
    # initialize length at 2 (length for 2)
    length = 2
    # initialize generator
    len_gen = gen_length(maximum)

    # start with 3, check all numbers up to maximum
    for i in range(3, maximum):
        # get length of chain for next integer
        i_length = next(len_gen)

        # check if longest so far; if so, update
        if i_length > length:
            length = i_length
            longest = i

    return longest, length


print(find_longest(1000000))
