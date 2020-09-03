""" Project Euler Problem 17. https://projecteuler.net/problem=17"""

# 1-9           90 times as final digit
# 1-9           100 times before "hundred"
# 10 to 19      10 times
# 20, 30 ... 90 10 * 10 times
# "and"         9*99 times
# "hundred"     900 times
# "one thousand" once

one_to_nine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
ten_to_nineteen = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
twenty_to_ninety = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6
the_and = 3
hundred = 7
one_thousand = 11

total = 190 * one_to_nine + 10 * ten_to_nineteen + 100 * twenty_to_ninety + 9 * 99 * the_and + 900 * hundred + \
        one_thousand

one_to_ninety_nine = one_to_nine + ten_to_nineteen + 10 * twenty_to_ninety + 8 * one_to_nine
plain_hundreds = one_to_nine + 9 * hundred
fancy_hundreds = plain_hundreds * 99 + 3 * 99 * 9 + one_to_ninety_nine * 9




