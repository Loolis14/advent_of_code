from enum import Enum


class Fixe(Enum):
    TOO_MUCH = 0
    ONE_ERROR_D = 1
    ONE_ERROR_I = 2
    SAFE = 3


def first_part(file: str) -> int:
    safe_reports = 0
    with open(file) as f:
        for line in f:
            levels = list(map(int, line.split()))
            increasing = False if levels[0] > levels[1] else True
            safe = True
            for i in range(1, len(levels)):
                if increasing and levels[i - 1] >= levels[i]:
                    safe = False
                    break
                if not increasing and levels[i - 1] <= levels[i]:
                    safe = False
                    break
                if abs(levels[i - 1] - levels[i]) > 3:
                    safe = False
                    break
            if safe:
                safe_reports += 1
    return safe_reports


def first_check(levels: list[int]) -> int:
    increase = 0
    decrease = 0
    error = 0
    for i in range(len(levels) - 1):
        if levels[i] > levels[i + 1]:
            decrease += 1
        if levels[i] < levels[i + 1]:
            increase += 1
        if levels[i] == levels[i + 1] or abs(levels[i] - levels[i + 1]) > 3:
            error += 1
    if min(increase, decrease) + error > 1:
        return Fixe.TOO_MUCH
    elif min(increase, decrease) + error == 1:
        if increase > decrease:
            return Fixe.ONE_ERROR_I
        else:
            return Fixe.ONE_ERROR_D
    else:
        return Fixe.SAFE


def remove_error(levels: list[int], sens: Fixe) -> list[int]:
    increasing = True if sens.value == 2 else False
    new_levels = [levels[0]]
    i = 1
    while i < len(levels):
        if levels[i] == new_levels[-1]:
            i += 1
            break
        if increasing and levels[i] < new_levels[-1]:
            i += 1
            break
        if not increasing and levels[i] > new_levels[-1]:
            i += 1
            break
        if levels[i] - new_levels[-1] > 3:
            i += 1
            break
        new_levels.append(levels[i])
        i += 1
    while i < len(levels):
        new_levels.append(levels[i])
        i += 1
    return new_levels


def second_part(file: str) -> int:
    safe_reports = 0
    with open(file) as f:
        for line in f:
            levels = list(map(int, line.split()))
            fixe_num = first_check(levels)
            if fixe_num == Fixe.TOO_MUCH:
                continue
            elif fixe_num == Fixe.SAFE:
                safe_reports += 1
                continue
            new_levels = remove_error(levels, fixe_num)
            second_fix_num = first_check(new_levels)
            if second_fix_num == Fixe.SAFE:
                safe_reports += 1
    return safe_reports


# print('First part solution is:', first_part('test2.txt'))
print('Second part solution is:', second_part('test2.txt'))

"""
First Version, december 2024

PART 1:
test = open("input_2.txt").read().splitlines()
safe = 0

for list in test:
    l2 = []

    for c in list.split():
        if c == " ":
            continue
        else:
            l2.append(int(c))

    if l2[0] < l2[1]:
        if l2 == sorted(l2):
            for i in range(len(l2)-1):
                if l2[i]==l2[i+1]:
                    break
                elif l2[i+1]-l2[i]>3:                   
                    break
            else:
                safe += 1

    elif l2[0] > l2[1]:
        if l2 == sorted(l2,reverse=True):
            for i in range(len(l2)-1):
                if l2[i]==l2[i+1]:                    
                    break
                elif l2[i]-l2[i+1]>3:                                        
                    break
            else:
                safe += 1

print(safe)
"""
