import re


def is_valid(s: str) -> bool:
    if not re.search(r'(.)\1', s):
        return False
    if re.search(r'ab|cd|pq|xy', s):
        return False
    if len(re.findall('[aeiou]', s)) <= 2:
        return False
    return True


def first_part(file: str) -> int:
    good_string = 0
    with open(file) as f:
        for line in f:
            if is_valid(line.strip('\n')):
                good_string += 1
    return good_string


def is_valid_regex(s: str) -> bool:
    if not re.search(r'([a-zA-Z]).\1', s):
        return False
    if not re.search(r'(.{2}).*\1', s):
        return False
    return True


def second_part(file: str) -> int:
    good_string = 0
    with open(file) as f:
        for line in f:
            if is_valid_regex(line.strip('\n')):
                good_string += 1
    return good_string


# print('First part result:', first_part('test1.txt'))
print('Second part result:', second_part('test2.txt'))
