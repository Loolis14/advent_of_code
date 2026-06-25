def adjacent_letter(x: int, y: int,
                    m_letter: set) -> list[tuple[int, int, int, int]]:
    adjacents = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in m_letter:
            adjacents.append((new_x, new_y, dx, dy))
    return adjacents


def first_part(file: str) -> int:
    letters = {'X': [], 'M': set(), 'A': set(), 'S': set()}
    with open(file) as f:
        for j, line in enumerate(f):
            for i, c in enumerate(line):
                if c in 'MAS':
                    letters[c].add((i, j))
                elif c == 'X':
                    letters[c].append((i, j))
    xmas_count = 0
    for x, y in letters['X']:
        adjacents = adjacent_letter(x, y, letters['M'])
        if not adjacents:
            continue
        for adjacent in adjacents:
            m_x, m_y, dx, dy = adjacent
            a_x, a_y = m_x + dx, m_y + dy
            if (a_x, a_y) not in letters['A']:
                continue
            s_x, s_y = a_x + dx, a_y + dy
            if (s_x, s_y) not in letters['S']:
                continue
            xmas_count += 1
    return xmas_count


def other_points_position(a_pos: tuple[int, int]) -> tuple[int, int, int, int]:
    x, y = a_pos
    hg_pos = (x - 1, y - 1)
    hd_pos = (x + 1, y - 1)
    bg_pos = (x - 1, y + 1)
    bd_pos = (x + 1, y + 1)
    return (hg_pos, hd_pos, bg_pos, bd_pos)


def is_a(coord: tuple[int, int], a_positions: set) -> bool:
    return coord in a_positions


def second_part(file: str) -> int:
    letters = {'M': set(), 'A': [], 'S': set(), 'X': set()}
    count_x_mas = 0
    with open(file) as f:
        for j, line in enumerate(f):
            for i, c in enumerate(line):
                if c in 'XMS':
                    letters[c].add((i, j))
                elif c == 'A':
                    if j == 0 or i == 0:
                        continue
                    letters[c].append((i, j))
    for letter in letters['A']:
        if letter[0] == i or letter[1] == j:
            continue
        positions = other_points_position(letter)
        hg_pos, hd_pos, bg_pos, bd_pos = positions
        if is_a(hg_pos, letters['A']) or is_a(hd_pos, letters['A']) or is_a(bg_pos, letters['A']) or is_a(bd_pos, letters['A']):
            continue
        if is_a(hg_pos, letters['X']) or is_a(hd_pos, letters['X']) or is_a(bg_pos, letters['X']) or is_a(bd_pos, letters['X']):
            continue
        if hg_pos in letters['M'] and bd_pos not in letters['S']:
            continue
        if hg_pos in letters['S'] and bd_pos not in letters['M']:
            continue
        if hd_pos in letters['M'] and bg_pos not in letters['S']:
            continue
        if hd_pos in letters['S'] and bg_pos not in letters['M']:
            continue
        count_x_mas += 1
    return count_x_mas


# print('First part result:', first_part('test1.txt'))
print('Second part result:', second_part('test2.txt'))
