"""
Euler Project #19. https://projecteuler.net/problem=19
"""

import datetime

count = 0

# cycle through every year
for i in range(1901, 2001):
    # cycle through every month
    for j in range(1, 13):
        # get the day of the week for the first of the month
        day = datetime.date(i, j, 1).weekday()
        # if it's Sunday, add to count
        if day == 6:
            count += 1

print(count)

# You can also get a good guess by dividing 1200 by 7 and rounding.
