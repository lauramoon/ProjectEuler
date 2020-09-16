"""
Project Euler Problem 21. https://projecteuler.net/problem=21
Amicable numbers: they come in pairs. The sum of the proper divisors of each
is equal to the other member of the pair.
"""


def divisor_sum(n):
    """
    calculates the sum of the proper divisors of an integer n,
    this includes 1 but not n in the sum
    :param n: a positive integer
    :return: integer sum of the proper divisors of n
    """
    # running sum of divisors
    # one is always a proper divisor, skip in loop
    total = 1

    # loop through 2 to half of n
    # (highest possible proper divisor is half of n)
    # could go to root n, but would have to account for perfect squares;
    # this is fast enough
    for i in range(2, n//2 + 1):
        if n % i == 0:
            total += i

    return total


def main():
    # create dictionary of amicable pairs, each as key with the other the value
    amicable = {}

    # loop through every integer under consideration
    for i in range(10000):
        # if already found, skip
        if i in amicable:
            continue

        # get sum of divisors
        d_sum = divisor_sum(i)

        # if the sum is larger, see if the sum's divisor sum is i
        if d_sum > i and divisor_sum(d_sum) == i:
            # put in dictionary, both ways
            amicable[i] = d_sum
            amicable[d_sum] = i
            print(i, d_sum)

    # sum of amicable numbers found
    total = 0

    # sum the numbers found (either the keys or the values)
    for key in amicable:
        total += key

    print(total)


main()