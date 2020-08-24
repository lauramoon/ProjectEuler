"""Project Euler Problem 11. https://projecteuler.net/problem=11
problem involves a 20x20 grid of two-digit numbers printed on the
problem webpage. This solution retrieves the numbers from the website"""
import requests
import bs4


def get_page():
    """
    gets the problem page from the web, saves to the same folder as this file.
    only need to run once, then just get info locally
    :return: none
    """
    res = requests.get("https://projecteuler.net/problem=11")
    f = open('prob11.txt', 'w')
    f.write(res.text)
    f.close()


def get_grid():
    """
    takes the 20x20 grid of numbers found on the webpage and puts it into a list of lists
    :return: 20-item list of 20-item lists
    """
    # get the html text from the file saved above
    f = open('prob11.txt', 'r')
    content = f.read()
    f.close()

    # turn it into a soup
    soup = bs4.BeautifulSoup(content, "lxml")
    # use the class that gets just the numbers
    grid = soup.select('.monospace.center')
    # keep only the text
    numbers = grid[0].text
    # turn it into a list
    number_list = numbers.split()
    # make the string numbers into integers
    for i in range(400):
        number_list[i] = int(number_list[i])

    # turn into grid
    number_grid = []

    for i in range(20):
        number_grid.append(number_list[i*20:i*20+20])

    return number_grid


def calc_products():
    grid = get_grid()
    greatest_product = 0

    # check rows of 4
    for line in grid:
        for i in range(17):
            product = line[i]*line[i+1]*line[i+2]*line[3]
            greatest_product = max(greatest_product, product)

    # check columns of 4
    for i in range(20):
        for j in range(17):
            product = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            greatest_product = max(greatest_product, product)

    # check NW to SE diagonals
    for i in range(17):
        for j in range(17):
            product = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            greatest_product = max(greatest_product, product)

    # check SW to NE diagonals
    for i in range(17):
        for j in range(17):
            product = grid[i+3][j]*grid[i+2][j+1]*grid[i+1][j+2]*grid[i][j+3]
            greatest_product = max(greatest_product, product)

    print(greatest_product)


calc_products()


