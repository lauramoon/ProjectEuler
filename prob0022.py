"""
Project Euler Problem 22. https://projecteuler.net/problem=22
"""
import requests


def get_names():
    """
    Get list of names from website, return as a list.
    :return: list of over 5000 first names.
    """
    file_path = "https://projecteuler.net/project/resources/p022_names.txt"
    r = requests.get(file_path)
    name_list = r.text.split('","')

    # have to remove the '"' at the beginning of the first name to sort properly
    name_list[0] = name_list[0][1:]

    sorted_list = sorted(name_list)

    print(sorted_list[0:10])

    return sorted_list


def calc_value(name):
    """
    Take name (string of letters) and calculate value as sum of the alphabetical position of the letters
    :param name: string, provided as upper case
    :return: integer value of sum of letter values
    """
    letter_map = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                  "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
                  "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, '"': 0}
    total = 0
    for char in name:
        total += letter_map[char]

    return total


def add_it_all_up():
    grand_total = 0

    name_list = get_names()
    i = 0

    for name in name_list:
        i += 1
        name_total = calc_value(name) * i
        grand_total += name_total

    print(grand_total)


add_it_all_up()
