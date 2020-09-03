"""Project Euler Problem 13. https://projecteuler.net/problem=13"""
import requests
import bs4


def get_page():
    """
    gets the problem page from the web, saves to the same folder as this file.
    only need to run once, then just get info locally
    """
    res = requests.get("https://projecteuler.net/problem=13")
    f = open('prob13.txt', 'w')
    f.write(res.text)
    f.close()


def get_list():
    """
    takes the list of really long integers on the webpage and puts them into a list
    :return: list of 100 50-digit integers
    """
    # get the html text from the file saved above
    f = open('prob13.txt', 'r')
    content = f.read()
    f.close()

    # turn it into a soup
    soup = bs4.BeautifulSoup(content, "lxml")
    # use the class that gets just the numbers
    text = soup.select('.monospace.center')
    # keep only the text
    numbers = text[0].text
    # turn it into a list
    number_list = numbers.split()
    # make the string numbers into integers
    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])

    return number_list


# get_page()
number_list = get_list()
# print(number_list)
print(sum(number_list))
