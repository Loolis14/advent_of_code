def first_part(file: str) -> int:
    number = None
    increasing = 0
    with open(file) as f:
        for line in f:
            line = int(line.strip('\n'))
            if not number:
                number = line
                continue
            if number < line:
                increasing += 1
            number = line
    return increasing


def second_part(file: str) -> int:
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(int(line.strip('\n')))
    acc_numbers = []
    i = 0
    while i < len(numbers) - 2:
        temp_number = 0
        for j in range(3):
            temp_number += numbers[i + j]
        acc_numbers.append(temp_number)
        i += 1
    current_value = None
    increasing = 0
    for i, n in enumerate(acc_numbers):
        if not current_value:
            current_value = n
        if n > current_value:
            increasing += 1
        current_value = n
    return increasing


# print('First part solution:', first_part('test1.txt'))
print('Second part solution:', second_part('test2.txt'))
