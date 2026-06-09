import copy

def second_part(original_obstacle, guard_position, seen, guard_direction, x, y):
    rotation = '^>v<'
    directions = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
    new_obstacles = list(seen)
    loop = 0
    while new_obstacles:
        current_x, current_y = guard_position
        direction = guard_direction
        index_direction = rotation.index(guard_direction)
        loop_detection = set()

        new_obstacle = new_obstacles.pop()
        test_obstacle = copy.copy(original_obstacle)
        test_obstacle.add(new_obstacle)
        while 0 <= current_x < x and 0 <= current_y < y:
            dx, dy = directions[direction]
            new_x, new_y = current_x + dx, current_y + dy
            if (new_x, new_y) in test_obstacle:
                index_direction = (index_direction + 1) % 4
                direction = rotation[index_direction]
            else:
                if (new_x, new_y, direction) in loop_detection:
                    loop += 1
                    break
                loop_detection.add((new_x, new_y, direction))
                current_x, current_y = new_x, new_y
    print(loop)


def first_part(file):
    obstacle_positions = set()
    rotation = '^>v<'
    with open(file) as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c == '#':
                    obstacle_positions.add((x, y))
                elif c in rotation:
                    guard_direction = c
                    index_direction = rotation.index(c)
                    guard_position = (x, y)
    seen = set()
    directions = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
    current_x, current_y = guard_position
    direction = guard_direction
    while 0 <= current_x < x and 0 <= current_y < y:
        dx, dy = directions[direction]
        new_x, new_y = current_x + dx, current_y + dy
        if (new_x, new_y) in obstacle_positions:
            index_direction = (index_direction + 1) % 4
            direction = rotation[index_direction]
        else:
            seen.add((new_x, new_y))
            current_x, current_y = new_x, new_y
    second_part(obstacle_positions, guard_position, seen, guard_direction, x, y)
    return len(seen)


print(first_part('test2.txt'))  # mon gros test
print(first_part('fichier.txt'))  # petit test
print(first_part('the-guard.txt'))  # gros test de Lou
