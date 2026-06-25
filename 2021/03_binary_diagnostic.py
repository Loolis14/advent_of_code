def first_part(file: str) -> int:
    occurences = [{'0': 0, '1': 0}, {'0': 0, '1': 0},
                  {'0': 0, '1': 0}, {'0': 0, '1': 0},
                  {'0': 0, '1': 0}, {'0': 0, '1': 0},
                  {'0': 0, '1': 0}, {'0': 0, '1': 0},
                  {'0': 0, '1': 0}, {'0': 0, '1': 0},
                  {'0': 0, '1': 0}, {'0': 0, '1': 0}]
    with open(file) as f:
        for line in f:
            line = line.strip('\n')
            for i, c in enumerate(line):
                occurences[i][c] += 1
    bits_max = ''
    bits_min = ''
    for index in occurences:
        bits_max += max(index, key=index.get)
        bits_min += min(index, key=index.get)
    return int(bits_min, 2) * int(bits_max, 2)


def count_digit(numbers: list[str], i: int) -> tuple:
    n_0, n_1 = 0, 0
    for n in numbers:
        if n[i] == '0':
            n_0 += 1
        else:
            n_1 += 1
    return n_0, n_1


def remove_wrong_digit(numbers: list[str], digit: str, i: int) -> list[str]:
    new_list = []
    for n in numbers:
        if n[i] == digit:
            new_list.append(n)
    return new_list


def find_less(numbers: list[str]) -> str:
    i = 1
    while len(numbers) > 1:
        n_0, n_1 = count_digit(numbers, i)
        if n_0 <= n_1:
            numbers = remove_wrong_digit(numbers, '0', i)
        else:
            numbers = remove_wrong_digit(numbers, '1', i)
        i += 1
    return numbers[0]


def find_max(numbers: list[str]) -> str:
    i = 1
    while len(numbers) > 1:
        n_0, n_1 = count_digit(numbers, i)
        if n_0 > n_1:
            numbers = remove_wrong_digit(numbers, '0', i)
        else:
            numbers = remove_wrong_digit(numbers, '1', i)
        i += 1
    return numbers[0]


def second_part(file: str) -> int:
    number_0 = []
    number_1 = []
    with open(file) as f:
        for line in f:
            line = line.strip('\n')
            if line[0] == '0':
                number_0.append(line)
            else:
                number_1.append(line)
    bits_max = find_less(min(number_0, number_1, key=len))
    bits_min = find_max(max(number_0, number_1, key=len))
    return int(bits_min, 2) * int(bits_max, 2)


# print('First part result:', first_part('test2.txt'))
print('Second part result:', second_part('test2.txt'))
