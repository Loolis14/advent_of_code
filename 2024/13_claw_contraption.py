# Cramer method was used is this problem.

import re


def calcul_difference(game: tuple) -> int:
    button_a, button_b, prize = game
    x_a, y_a = button_a
    x_b, y_b = button_b
    return abs(x_a * y_b - y_a * x_b)


def calcul_push(price: tuple, button: tuple, difference: int) -> int:
    x_b, y_b = button
    x_prize, y_prize = price
    if (x_prize * y_b - y_prize * x_b) % difference == 0:
        return abs(x_prize * y_b - y_prize * x_b) // difference
    return -1


def first_part(file: str) -> int:
    pattern_button = re.compile(r'X([+|-]\d+), Y([+|-]\d+)')
    pattern_price = re.compile(r'X=(\d+), Y=(\d+)')
    games = []

    with open(file) as f:
        for line in f:
            if 'Button A' in line:
                button_a = re.findall(pattern_button, line)
                button_a = (int(button_a[0][0]), int(button_a[0][1]))
            elif 'Button B' in line:
                button_b = re.findall(pattern_button, line)
                button_b = (int(button_b[0][0]), int(button_b[0][1]))
            elif 'Prize' in line:
                prize = re.findall(pattern_price, line)
                prize = (int(prize[0][0]), int(prize[0][1]))
                games.append((button_a, button_b, prize))

    cost = 0
    for game in games:
        difference = calcul_difference(game)
        push_b = calcul_push(game[2], game[0], difference)
        push_a = calcul_push(game[2], game[1], difference)
        if push_b == -1 or push_a == -1:
            continue
        cost += push_b + 3 * push_a

    return cost


def calcul_difference_2(game: tuple) -> int:
    button_a, button_b, prize = game
    x_a, y_a = button_a
    x_b, y_b = button_b
    return abs(x_a * y_b - y_a * x_b)


def calcul_push_2(price: tuple, button: tuple, difference: int) -> int:
    x_b, y_b = button
    x_prize, y_prize = price
    x_prize, y_prize = x_prize + 10000000000000, y_prize + 10000000000000
    if (x_prize * y_b - y_prize * x_b) % difference == 0:
        return abs(x_prize * y_b - y_prize * x_b) // difference
    return -1


def second_part(file: str) -> int:
    pattern_button = re.compile(r'X([+|-]\d+), Y([+|-]\d+)')
    pattern_price = re.compile(r'X=(\d+), Y=(\d+)')
    games = []

    with open(file) as f:
        for line in f:
            if 'Button A' in line:
                button_a = re.findall(pattern_button, line)
                button_a = (int(button_a[0][0]), int(button_a[0][1]))
            elif 'Button B' in line:
                button_b = re.findall(pattern_button, line)
                button_b = (int(button_b[0][0]), int(button_b[0][1]))
            elif 'Prize' in line:
                prize = re.findall(pattern_price, line)
                prize = (int(prize[0][0]), int(prize[0][1]))
                games.append((button_a, button_b, prize))

    cost = 0
    for game in games:
        difference = calcul_difference_2(game)
        push_b = calcul_push_2(game[2], game[0], difference)
        push_a = calcul_push_2(game[2], game[1], difference)
        if push_b == -1 or push_a == -1:
            continue
        cost += push_b + 3 * push_a

    return cost


# print('First part result:', first_part('test2.txt'))
print('Second part result:', second_part('test2.txt'))
