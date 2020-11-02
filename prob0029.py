"""
Project Euler Problem 29: Distinct Powers
because python handles large integers easily, this one is simple
"""

combos = set()

for i in range(2, 101):
    for j in range(2, 101):
        combos.add(i**j)

print(len(combos))
