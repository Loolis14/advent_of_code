def first_part() -> int:
    position_a = set()
    with open('test1.txt') as f:
        for y, line in enumerate(f):
            line = line.strip('\n')
            for x, c in enumerate(line):
                if c == '@':
                    position_a.add((x, y))
    directions = [(0, 1), (1, 1), (1, 0), (-1, 0), (0, -1),
                  (-1, -1), (1, -1), (-1, 1)]
    rolls_to_take = 0
    while True:
        less_than_4 = set()
        for curr_x, curr_y in position_a:
            count = 0
            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy
                if (new_x, new_y) in position_a:
                    count += 1
            if count < 4:
                rolls_to_take += 1
                less_than_4.add((curr_x, curr_y))
        if not less_than_4:
            break
        position_a ^= less_than_4

    return rolls_to_take


print(first_part())
