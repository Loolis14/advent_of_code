from functools import lru_cache


def first_part(file: str) -> None:
    with open(file) as f:
        content = f.readline().split()
    for _ in range(25):
        split = False
        for i, n in enumerate(content):
            if split:
                split = False
                continue
            if n == '0':
                content[i] = '1'
            elif len(n) % 2 == 0:
                content[i] = n[:len(n) // 2]
                second_number = n[len(n) // 2:]
                content.insert(i + 1, str(int(second_number)))
                split = True
            else:
                content[i] = str(int(n) * 2024)
    return len(content)


def second_part(file: str) -> int:
    with open(file) as f:
        content = list(map(int, f.readline().split()))

    @lru_cache(maxsize=None)
    def count_stones(number: int, loop_left: int):
        if loop_left == 0:
            return 1
        if number == 0:
            return count_stones(1, loop_left - 1)
        n_str = str(number)
        if len(n_str) % 2 == 0:
            n1 = int(n_str[:len(n_str) // 2])
            n2 = int(n_str[len(n_str) // 2:])
            return (count_stones(n1, loop_left - 1) +
                    count_stones(n2, loop_left - 1))
        else:
            return count_stones(number * 2024, loop_left - 1)
    return sum(count_stones(n, 75) for n in content)


# print('First part result:', first_part('test1.txt'))
print('Second part result:', second_part('test2.txt'))
