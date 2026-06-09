def first_part() -> int:
    with open('test2.txt') as f:
        count = 0
        for line in f:
            line = line.strip('\n')
            i = 9
            for _ in range(9):
                if str(i) not in line:
                    i -= 1
                else:
                    if line.index(str(i)) == len(line) - 1:
                        i -= 1
                    else:
                        index_start = line.index(str(i))
                        start = i
                        break
            second = max(line[index_start + 1:])
            count += int(start) * 10 + int(second)
    return count


def second_part() -> int:
    with open('test2.txt') as f:
        count = 0
        for line in f:
            line = line.strip('\n')
            left = list(line)
            remove_n = len(left) - 12
            i = 0
            while i < len(left) - 1 and remove_n > 0:
                if left[i] < left[i + 1]:
                    while left[i] < left[i + 1] and remove_n > 0:
                        left.remove(left[i])
                        remove_n -= 1
                        if i != 0:
                            i -= 1
                else:
                    i += 1
            x = int(left[0])
            for i in range(1, 12):
                x = x * 10 + int(left[i])
            count += x
    return count


print('First part result: ', first_part())
print('Second part result: ', second_part())
