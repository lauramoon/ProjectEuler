"""
Project Euler Problem 30: Digit Fifth Powers https://projecteuler.net/problem=30
"""

# The sum of the numbers meeting the criteria
grand_total = 0

# Numbers must be less than 300,000 (2^5 + 9^5 + 9^5 + 9^5 + 9^5 =9^5 = 295,277)
# check each integer from 10 to 300,000
for i in range(10, 300000):
    # get the digits of i
    digits = list(str(i))
    # sum the fifth power of each digit
    total = sum([int(x)**5 for x in digits])

    # compare the total with i
    if i == total:
        print(i)
        # add to grand_total if they match
        grand_total += i

# the answer
print(grand_total)