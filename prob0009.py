"""Project Euler Problem 9. https://projecteuler.net/problem=9"""


def pythagorean_triplet(n: int) -> tuple:
    """
    searches for a Pythagorean triplet a^2 + b^2 = c^2 where
    a + b + c = n and a < b < c
    :param n: integer that is the sum of the integers in a Pythagorean triplet
    :return: the tuple in the form of (a, b, c) that sums to n. If none, (0, 0, 0)
    """
    # the lowest number in the triplet can't be higher than n/3
    a_high = int(n/3)

    # start with a_high, go down, check possible triplets
    # that sum to n to see if they're Pythagorean triplets
    for a in range(a_high, 0, -1):
        # b has to be higher than a, but lower than c
        b_high = int((n-a)/2)
        for b in range(a+1, b_high + 1):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a, b, c

    return 0, 0, 0


triplet = pythagorean_triplet(1000)
print(triplet)
print(triplet[0]*triplet[1]*triplet[2])

