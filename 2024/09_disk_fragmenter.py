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


print('First part solution:', first_part('test2.txt'))
