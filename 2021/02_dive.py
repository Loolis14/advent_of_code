def first_part(file: str) -> int:
    horizontal = 0
    depth = 0
    with open(file) as f:
        for line in f:
            content = line.split()
            command = content[0]
            n = int(content[1])
            if command == 'forward':
                horizontal += n
            elif command == 'up':
                depth -= n
            elif command == 'down':
                depth += n
    return horizontal * depth


def second_part(file: str) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    with open(file) as f:
        for line in f:
            content = line.split()
            command = content[0]
            n = int(content[1])
            if command == 'forward':
                horizontal += n
                depth = depth + aim * n
            elif command == 'up':
                aim -= n
            elif command == 'down':
                aim += n
    return horizontal * depth


# print('First part result:', first_part('test2.txt'))
print('Second part result:', second_part('test2.txt'))
