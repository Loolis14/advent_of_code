from collections import deque


def unpacking(disk_map: str) -> list[int]:
    unpack_disk_map = []
    index = 0
    for i, c in enumerate(disk_map):
        if i % 2:
            for _ in range(int(c)):
                unpack_disk_map.append('.')
        else:
            for _ in range(int(c)):
                unpack_disk_map.append(index)
            index += 1
    return unpack_disk_map


def regrouping(disk: list[int]) -> list[int]:
    n_number = len(disk) - disk.count('.')
    left = 0
    right = len(disk) - 1
    while n_number > 0:
        if disk[left] == '.':
            if not isinstance(disk[right], int):
                while right >= left and not isinstance(disk[right], int):
                    right -= 1
            disk[left], disk[right] = disk[right], disk[left]
            right -= 1
            left += 1
            n_number -= 1
        else:
            left += 1
            n_number -= 1
    return disk


def disk_sum(disk) -> int:
    acc = 0
    for i, c in enumerate(disk):
        if c == '.':
            break
        acc += i * c
    return acc


def first_part(file) -> int:
    disk_map = ''
    with open(file) as f:
        disk_map = f.readline()
    unpack_disk_map = unpacking(disk_map)
    regroup_disk_map = regrouping(unpack_disk_map)
    return disk_sum(regroup_disk_map)


def better_to_read(disk_map: str) -> list[tuple]:
    number_map = []
    index = 0
    number = 0
    for i, n in enumerate(disk_map):
        if i % 2 == 0:
            number_map.append((number, (index + int(n) - 1) - index + 1))
            number += 1
        if i % 2 != 0:
            number_map.append(('.', (index + int(n) - 1) - index + 1))
        index += int(n)
    return number_map


def number_to_move(number_map: list[tuple]) -> deque[tuple[int, int]]:
    numbers_to_fill = []
    for i, (n, how_many) in enumerate(number_map[::-1]):
        if isinstance(n, int):
            numbers_to_fill.append((how_many, n, len(number_map) - i - 1))
    return deque(numbers_to_fill)


def second_part(file) -> int:
    disk_map = ''
    with open(file) as f:
        disk_map = f.readline()
    number_map = better_to_read(disk_map)
    numbers_to_fill = number_to_move(number_map)
    final_map = []
    place_left = 0
    change = []
    change_index = []
    print('to fill', numbers_to_fill)
    print('original', number_map)
    i = 0
    while i < len(number_map):
        if not numbers_to_fill:
            break
        if place_left == 0 and isinstance(number_map[i][0], int):
            final_map.append(number_map[i])
            numbers_to_fill.pop()
            i += 1
        if place_left == 0 and isinstance(number_map[i][0], str):
            place_left = number_map[i][1]
            while numbers_to_fill and place_left != 0:
                weight, number_to_try, index = numbers_to_fill.popleft()
                if weight <= place_left:
                    place_left -= weight
                    final_map.append((number_to_try, weight))
                    change.append((weight, number_to_try, index))
                    change_index.append(index)
                    if place_left == 0:
                        i += 1
                if weight > place_left:
                    continue
    print("FINAL", final_map)
    print(i)
    print(change)
    index = change_index.pop()
    while i < len(number_map):
        if i == index:
            final_map.append('ICI')
            if change_index:
                index = change_index.pop()
        else:
            final_map.append(number_map[i])
        i += 1
    print("FINAL", final_map)


def number_to_move_2(disk_map) -> None:
    number_map = []
    index = 0
    number = 0
    for i, n in enumerate(disk_map):
        if i % 2 == 0:
            number_map.append((number, (index + int(n) - 1) - index + 1))
            number += 1
        if i % 2 != 0:
            number_map.append(('.', (index + int(n) - 1) - index + 1))
        index += int(n)
    return number_map


def second_part_2(file: str) -> None:
    disk_map = ''
    with open(file) as f:
        disk_map = f.readline()
    unpack_disk = unpacking(disk_map)
    print(unpack_disk)
    number_to_move_2(disk_map)


# print('First part solution:', first_part('test2.txt'))
print('Second part solution:', second_part_2('test1.txt'))
