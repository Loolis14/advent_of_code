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


print('First part result:', first_part('test1.txt'))
