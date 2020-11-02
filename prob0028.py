"""
Project Euler Problem 28: Number spiral diagonals https://projecteuler.net/problem=28
The (4*i^2 + i + 1) formula was worked out algebraically on paper.
The spiral can be thought of as 500 concentric squares with a 1 in the middle.
The sum of the corners of each square equals 4 times the value located in the middle
of the left side of each square. Some experimentation yields this formula to calculate
this value.
"""

total = 1
for i in range(1, 501):
    total += (4*i*i + i + 1) * 4

print(total)
