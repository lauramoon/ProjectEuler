"""Project Euler Problem 6. https://projecteuler.net/problem=6"""


sum_of_squares = sum([i**2 for i in range(1, 101)])
square_of_sums = (sum(range(1, 101)))**2
print(sum_of_squares)
print(square_of_sums)
print(sum_of_squares - square_of_sums)

