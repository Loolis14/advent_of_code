from collections import deque


def first_part(file):
    spittler_positions = set()
    with open(file) as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                if c == '^':
                    spittler_positions.add((j, i))
                if c == 'S':
                    initial_position = (j, i)
    max_y = i
    max_x = j
    stack = deque([initial_position])
    positions_seen = set()
    split = 0

    while stack:
        change = False
        curr_x, curr_y = stack.popleft()
        new_x, new_y = curr_x, curr_y + 1
        if new_y > max_y:
            continue
        if (new_x, new_y) in spittler_positions:
            right_x, left_x = new_x + 1, new_x - 1
            if right_x <= max_x and (right_x, new_y) not in positions_seen:
                change = True
                positions_seen.add((right_x, new_y))
                stack.append((right_x, new_y))
            if left_x >= 0 and (left_x, new_y) not in positions_seen:
                change = True
                positions_seen.add((left_x, new_y))
                stack.append((left_x, new_y))
        else:
            stack.append((new_x, new_y))
        if change:
            split += 1
    return split


print(first_part('test2.txt'))
