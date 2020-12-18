'''Project Euler Problem #31: https://projecteuler.net/problem=31'''


def calc_value(numbers):
    """
    Given a list of numbers of coins, calculate the value
    :param numbers: list of the number of each type of coin
    :return: the value of the coins
    """
    coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
    total = 0
    for i in range(len(coin_values)):
        total += numbers[i]*coin_values[i]
    return total


def count_ways_wrapper(goal):
    """
    wrapper for recursive count ways function
    """
    ways = 0
    current_set = [0]*8
    ways, current_set = count_ways(goal, 0, ways, current_set)
    return ways, current_set


def count_ways(goal, position, ways, current_set):
    """
    given a total value, how many ways can you get that value? calculates recursively
    can always add pennies to totals under goal, so don't consider position 7
    :param goal: the total value (2 pounds or 200p in the problem)
    :param position: position in list of coins to consider
    :param ways: total number of ways found so far
    :param current_set: current set of coins being considered
    """
    while calc_value(current_set) <= goal:
        if position < 6:
            ways, current_set = count_ways(goal, position+1, ways, current_set)

        else:
            if calc_value(current_set) <= goal:
                ways += 1

        current_set[position] += 1

        if calc_value(current_set) > goal:
            current_set[position] = 0
            break

    return ways, current_set


print(count_ways_wrapper(200))
