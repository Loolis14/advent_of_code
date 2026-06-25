import re


def parsing(file: str) -> list[tuple]:
    vents = []
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    with open(file) as f:
        for line in f:
            coord = re.findall(pattern, line)
            sx, sy = int(coord[0][0]), int(coord[0][1])
            ex, ey = int(coord[0][2]), int(coord[0][3])
            vents.append((sx, sy, ex, ey))
    return vents


def remove_diagonal(vents: list[tuple]) -> list[tuple]:
    vents_without_diagonal = []
    for vent in vents:
        sx, sy, ex, ey = vent
        if sx == ex or sy == ey:
            vents_without_diagonal.append(vent)
    return vents_without_diagonal


def first_part(vents: list[tuple]) -> int:
    vents_clean = remove_diagonal(vents)
    all_points = {}
    for vent in vents_clean:
        sx, sy, ex, ey = vent
        if sy == ey:
            for i in range(min(ex, sx), max(ex, sx) + 1):
                all_points[(i, sy)] = all_points.get((i, sy), 0) + 1
        else:
            for i in range(min(ey, sy), max(ey, sy) + 1):
                all_points[(sx, i)] = all_points.get((sx, i), 0) + 1
    return sum(1 for v in all_points.values() if v > 1)


def second_part(vents: list[tuple]) -> int:
    all_points = {}
    for vent in vents:
        sx, sy, ex, ey = vent
        if sy == ey:
            for i in range(min(ex, sx), max(ex, sx) + 1):
                all_points[(i, sy)] = all_points.get((i, sy), 0) + 1
        elif sx == ex:
            for i in range(min(ey, sy), max(ey, sy) + 1):
                all_points[(sx, i)] = all_points.get((sx, i), 0) + 1
        else:
            dx = -1 if sx > ex else 1
            dy = -1 if sy > ey else 1
            while sx != ex:
                all_points[(sx, sy)] = all_points.get((sx, sy), 0) + 1
                sx, sy = sx + dx, sy + dy
            all_points[(sx, sy)] = all_points.get((sx, sy), 0) + 1

    return sum(1 for v in all_points.values() if v > 1)


if __name__ == '__main__':
    vents = parsing('test2.txt')
    print('First part result', first_part(vents))
    print('Second part result', second_part(vents))
