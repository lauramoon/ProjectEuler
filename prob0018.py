"""
Project Euler #18 https://projecteuler.net/problem=18
"""
import requests
import bs4


def get_page():
    """
    get the webpage with the problem and save locally
    """
    path = "https://projecteuler.net/problem=18"
    r = requests.get(path)
    file_path = "prob18.txt"
    file = open(file_path, 'w')
    file.write(r.text)
    file.close()


def get_data():
    """
    decipher the webpage
    :return: list of rows, each a list of numbers in the row
    """
    # get the page stored locally
    file_path = "prob18.txt"
    file = open(file_path, 'r')
    html = file.read()
    file.close()
    # turn the page into a soup
    soup = bs4.BeautifulSoup(html, "lxml")

    # pull the numbers from the pyramid out
    numbers = soup.select(".monospace")
    # split them into lines
    lines = numbers[1].text.split("\n")

    # the variable for the final list of lists
    pyramid = []

    # go through each line of numbers
    for line in lines:
        # split the string at the spaces
        string_list = line.split()
        # create a list for the numbers
        number_list = []
        # go through the list of number strings
        for number in string_list:
            # make new list with numbers as integers
            number_list.append(int(number))
        # append the list of numbers to the pyramid
        pyramid.append(number_list)

    return pyramid


def find_max_path():
    """
    Use the pyramid data to find the max path through it. Note that this solution does not track what that path is;
    it simply finds the maximum sum from traversing down the pyramid.
    """
    pyramid = get_data()
    # new pyramid, with each entry the max sum of a path from the tip
    # initialize with number at the tip
    max_pyramid = [[75]]

    # go through remaining lines of the pyramid
    for i in range(1, len(pyramid)):
        # create new line for max pyramid
        max_line = []
        # get the max number immediately above to right or left
        for j in range(0, i+1):
            # only one option for end numbers
            if j == 0:
                max_add = max_pyramid[i-1][0]
            elif j == i:
                max_add = max_pyramid[i-1][j-1]
            # pick the max of the two above
            else:
                max_add = max(max_pyramid[i-1][j-1], max_pyramid[i-1][j])

            # add this max to the number in the pyramid
            max_line.append(max_add + pyramid[i][j])

        # append this line to the max pyramid
        max_pyramid.append(max_line)

    print(max_pyramid)


find_max_path()
