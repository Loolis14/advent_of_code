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

# (?s) permet d'activer le DOTALL qui permet au point de prendre en
# compte les \n également
