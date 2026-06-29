import re


def first_part(file: str) -> int:
    with open(file) as f:
        corrupted_file = f.read()
        not_corrupted = re.findall(r'mul[(](\d+),(\d+)[)]', corrupted_file)
        mull = sum(int(a) * int(b) for a, b in not_corrupted)
        return mull


def second_part(file: str) -> int:
    with open(file) as f:
        corrupted_file = f.read()
        without_dont = re.sub(
            r"(?s)(don't[(][)].*?)(do[(][)]|$)", "", corrupted_file)
        not_corrupted = re.findall(r"mul[(](\d+),(\d+)[)]", without_dont)
        mull = sum(int(a) * int(b) for a, b in not_corrupted)
        return mull


print('First part solution:', first_part('test2.txt'))
print('Second part solution:', second_part('test2.txt'))

"""
First Version, december 2024

import re
test = open("input_3.txt").read()
regex = re.compile(r'mul\((\d+),(\d+)\)')
delete = re.sub(r'(?<=don\'t\(\))(.*?)(?=do\(\))', "", test, flags=re.DOTALL)



f = regex.findall(delete)
acc = 0
for match in f:
    a,b = match
    acc += int(a) * int(b)
print(acc) #+triche
"""
