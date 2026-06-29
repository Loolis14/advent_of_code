import re


def parsing(file: str) -> list[tuple]:
    robots = []
    with open(file) as f:
        for line in f:
            robots.append(re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line))
    return robots


def remove_middle(positions: list[tuple]) -> int:
    middle_x, middle_y = 101 // 2, 103 // 2
    robots_hg, robots_hd, robots_bg, robots_bd = 0, 0, 0, 0
    for x, y in positions:
        if x == middle_x or y == middle_y:
            continue
        else:
            if x < middle_x and y < middle_y:
                robots_hg += 1
            elif x > middle_x and y < middle_y:
                robots_hd += 1
            elif x < middle_x and y > middle_y:
                robots_bg += 1
            elif x > middle_x and y > middle_y:
                robots_bd += 1
    return robots_hg * robots_hd * robots_bg * robots_bd


def first_part(robots: list[tuple]) -> int:
    new_positions = []
    for robot in robots:
        x_pos, y_pos, v_x, v_y = map(int, robot[0])
        new_position = (x_pos + v_x * 100) % 101, (y_pos + v_y * 100) % 103
        new_positions.append(new_position)
    nb_robots = remove_middle(new_positions)
    return nb_robots


if __name__ == '__main__':
    robots = parsing('test1.txt')
    print('First part result:', first_part(robots))
