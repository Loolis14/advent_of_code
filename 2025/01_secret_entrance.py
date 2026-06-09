def second_part(lines: list[str]) -> int:
    start = 50
    count_0 = 0
    for content in lines:
        number = int(content[1:])
        count_0 += number // 100
        number = number % 100
        if content[0] == 'L':
            temp = (start - number) % 100
            if start != 0 and temp != 0 and temp >= start:
                count_0 += 1
        elif content[0] == 'R':
            temp = (start + number) % 100
            if start != 0 and temp != 0 and temp <= start:
                count_0 += 1
        if temp == 0:
            count_0 += 1
        start = temp
    return count_0


def first_part() -> int:
    start = 50
    count_0 = 0

    with open('test1.txt') as f:
        lines = f.read().splitlines()

    print('Second part result: ', second_part(lines))

    for content in lines:
        number = int(content[1:])
        if content[0] == 'L':
            temp = (start - number) % 100
        elif content[0] == 'R':
            temp = (start + number) % 100
        if temp == 0:
            count_0 += 1
        start = temp

    return count_0


print('First part result: ', first_part())
