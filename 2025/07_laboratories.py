from collections import deque
from functools import lru_cache


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


def second_part_iterative(file) -> int:
    spittler_positions = set()
    with open(file) as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                if c == '^':
                    spittler_positions.add((j, i))
                if c == 'S':
                    initial_position = (j, i)
    max_y = i
    stack = deque([(initial_position, {initial_position})])
    position_seen = set()
    possible_path = 0
    while stack:
        current_pos, path = stack.popleft()
        new_x, new_y = current_pos[0], current_pos[1] + 1
        if new_y == max_y:
            position_seen |= path
            possible_path += 1
            continue
        new_position = (new_x, new_y)
        if new_position in position_seen:
            continue
        if new_position in spittler_positions:
            left = (new_x - 1, new_y)
            right = (new_x + 1, new_y)
            if left not in position_seen:
                stack.append((left, path | {left}))
            if right not in position_seen:
                stack.append((right, path | {right}))
        else:
            stack.append((new_position, path | {new_position}))
    return possible_path


def second_part_recursive(file) -> int:
    spittler_positions = set()
    with open(file) as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                if c == '^':
                    spittler_positions.add((j, i))
                if c == 'S':
                    initial_position = (j, i)
    max_y = j
    max_path = 0

    @lru_cache
    def bfs(position):
        if position[1] == max_y:
            return 1
        new_position = position[0], position[1] + 1
        if new_position in spittler_positions:
            left = (new_position[0] - 1, new_position[1])
            right = (new_position[0] + 1, new_position[1])
            return bfs(right) + bfs(left)
        return bfs(new_position)

    max_path += bfs(initial_position)
    return max_path


# print('First part', first_part('test2.txt'))
print('Second part:', second_part_recursive('test2.txt'))
