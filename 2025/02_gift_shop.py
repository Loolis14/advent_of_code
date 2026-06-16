import re


def is_valid_first(n: str) -> bool:
    len_n = len(n)
    if len_n % 2 != 0:
        return True
    middle = len_n // 2
    return n[:middle] == n[middle:]


def is_valid_second(n: str) -> bool:
    if re.fullmatch(r'(.+)\1+', n):
        return False
    return True


def part_one(file) -> int:
    invalid_id_sum = 0
    with open(file) as f:
        content = f.read()
        ranges = content.split(',')
    for range_ in ranges:
        start, end = range_.split('-')
        start, end = int(start), int(end)
        for i in range(start, end + 1):
            if not is_valid_second(str(i)):
                invalid_id_sum += i
    return invalid_id_sum


# print('First Part solution:', part_one('test2.txt'))
print('First Part solution:', part_one('test2.txt'))
