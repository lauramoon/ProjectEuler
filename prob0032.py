"""
Project Euler Problem 32. https://projecteuler.net/problem=32

As each multiplication sentence must have nine digits total, the product must have 4 digits,
with the other two numbers having either 2 and 3 digits or 1 and 4 digits

No number can contain 0's, and the last digit cannot be 5.
"""


def is_eligible(number) -> bool:
    """
    Checks if number includes 0, ends in 5, or has duplicate digits
    :param number: integer being checked
    :return boolean: true if number eligible
    """
    string = str(number)
    length = len(string)
    result = True

    # check for duplicates
    if len(set(string)) != length:
        result = False

    # check if contains 0 or ends in 5
    if "0" in string or string[-1] == 5:
        result = False

    return result


def main():
    # Sum of qualifying products
    total = 0

    # Loop through all potential 4-digit numbers, starting with the lowest to qualify
    for i in range(1234, 9877):
        # check if eligible
        if is_eligible(i) is False:
            continue

        # consider 1- and 2-digit multiplicands
        for j in range(2, 99):
            # check eligibility
            if is_eligible(j) is False:
                continue

            # check if factor
            if i % j != 0:
                continue

            # check that other factor is eligible
            if is_eligible(i//j) is False:
                continue

            # check if the string of the three numbers has 9 digits and no duplicates
            string = str(i) + str(j) + str(i//j)
            if len(string) == 9 and len(set(string)) == 9:
                total += i
                print(string)
                print(total)

                # no need to continue checking this product
                break


main()
