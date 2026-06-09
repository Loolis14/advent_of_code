def second_part(file):
    with open(file) as f:
        lines = f.read().splitlines()
    str_numbers = lines[:-1]
    symbols = lines[-1]
    numbers_at_index = {}
    for str_nums in str_numbers:
        for i, n in enumerate(str_nums):
            if n != ' ':
                numbers_at_index[i] = numbers_at_index.get(i, 0) * 10 + int(n)
    numbers = []
    for i in range(len(symbols)):
        symbol = symbols[i]
        if symbol in '*+':
            start = i
            i += 1
            while i < len(symbols) and symbols[i] == ' ':
                i += 1
            if i == len(symbols):
                end = len(lines[0]) - 1
            else:
                end = i - 2
            if symbol == '*':
                temp_numbers = 1
                for i in range(start, end + 1):
                    temp_numbers *= numbers_at_index[i]
                numbers.append(temp_numbers)
            else:
                temp_numbers = 0
                for i in range(start, end + 1):
                    temp_numbers += numbers_at_index[i]
                numbers.append(temp_numbers)
    return sum(numbers)


def first_part(file):
    parsing = {'*': None, '+': None}
    with open(file) as f:
        for i, line in enumerate(f):
            if i == 0:
                numbers = list(map(int, line.split()))
                parsing['*'] = numbers
                parsing['+'] = numbers[:]
            else:
                if line[0] in '*+':
                    last_line = line.split()
                    break
                for j, n in enumerate(line.split()):
                    number = int(n.strip())
                    parsing['*'][j] *= number
                    parsing['+'][j] += number
    acc = 0
    for i, c in enumerate(last_line):
        acc += parsing[c][i]
    return acc


print('First part result: ', first_part('test2.txt'))
print('Second part result: ', second_part('test2.txt'))
