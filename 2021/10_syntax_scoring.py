from typing import Union


def found_illegal(line: str) -> Union[str, list[str]]:
    character_match = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            matching_character = stack.pop()
            if character_match[matching_character] == c:
                continue
            return c
    return stack


def calcul_completing_char(illegal_characters: list[str]) -> int:
    character_completing_weight = {'(': 1, '[': 2, '{': 3, '<': 4}
    total = 0
    for char in illegal_characters[::-1]:
        total = total * 5 + character_completing_weight[char]
    return total


def first_part(file: str, part: int) -> int:
    character_weight = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total_syntax_error = 0
    completing_syntax = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            illegal_char = found_illegal(line)
            if isinstance(illegal_char, str):
                total_syntax_error += character_weight[illegal_char]
                continue
            if isinstance(illegal_char, list):
                if not illegal_char:
                    continue
                completing_syntax.append(calcul_completing_char(illegal_char))
    if part == 2:
        middle = len(completing_syntax) // 2
        return sorted(completing_syntax)[middle]
    return total_syntax_error


print('First part result:', first_part('test2.txt', 2))
