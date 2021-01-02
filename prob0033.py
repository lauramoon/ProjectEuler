"""
Project Euler Problem 33: https://projecteuler.net/problem=33
"""
# This code identifies the 4 qualifying fractions. The remainder of the problem
# can be completed mentally.

for i in range(11, 100):
    for j in range(10, i):
        n0 = str(j)[0]
        n1 = str(j)[1]
        d0 = str(i)[0]
        d1 = str(i)[1]

        if n0 == d1 and d0 != '0' and int(n1)/int(d0) == j/i:
            print(f"{j}/{i}")
        if n1 == d0 and d1 != '0' and int(n0)/int(d1) == j/i:
            print(f"{j}/{i}")

