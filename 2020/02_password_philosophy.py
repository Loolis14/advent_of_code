import re
from collections import Counter


def first_part(file: str) -> int:
    valid_password = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            rules, password = line.split(':')
            min_occ, max_occ, letter = re.findall(r'^(\d+)-(\d+) ([a-z])$', rules)[0]
            if int(min_occ) <= Counter(password.strip())[letter] <= int(max_occ):
                valid_password += 1
    return valid_password


def second_part(file: str) -> int:
    valid_password = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            rules, password = line.split(':')
            right_idx, wrong_idx, letter = re.findall(r'^(\d+)-(\d+) ([a-z])$', rules)[0]
            idx_1 = int(right_idx) - 1
            idx_2 = int(wrong_idx) - 1
            password = password.strip()
            first, second = password[idx_1], password[idx_2]
            if first == second:
                continue
            if first == letter or second == letter:
                valid_password += 1
    return valid_password


# print('First part solution:', first_part('test2.txt'))
print('Second part solution:', second_part('test2.txt'))
