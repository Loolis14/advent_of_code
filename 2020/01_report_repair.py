def first_part(file: str) -> int:
    lefts_seen = set()
    with open(file) as f:
        for line in f:
            number = int(line.rstrip('\n'))
            left = 2020 - number
            if left in lefts_seen:
                return number * (2020 - number)
            lefts_seen.add(number)


def second_part(file: str) -> None:
    sum_possible = {}
    numbers = []
    with open(file) as f:
        for line in f:
            number = int(line.rstrip('\n'))
            left = 2020 - number
            if sum_possible.get(left):
                a, b = sum_possible.get(left)
                return a * b * number
            if numbers:
                for n in numbers:
                    sum_possible[n + number] = (n, number)
            numbers.append(number)


# print('First part:', first_part('test2.txt'))
print('Second part:', second_part('test2.txt'))
