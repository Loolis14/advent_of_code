def first_part(total, numbers) -> int:
    acc = 0

    def dfs(i, operation) -> None:
        if i == len(numbers):
            return operation == total
        return (dfs(i + 1, operation + numbers[i])
                or
                dfs(i + 1, operation * numbers[i]))

    if dfs(1, numbers[0]):
        acc += total
    return acc


def second_part(total, numbers) -> int:
    if len(numbers) == 2:
        if int(str(numbers[0]) + str(numbers[1])) == total:
            return total
        else:
            return 0
    acc = 0

    def dfs(i, operation) -> bool:
        if i == len(numbers):
            return operation == total
        return (dfs(i + 1, operation + numbers[i])
                or
                dfs(i + 1, operation * numbers[i])
                or
                dfs(i + 1, int(str(operation) + str(numbers[i]))))

    if dfs(1, numbers[0]):
        acc += total
    return acc


def bridge_repair(file: str) -> None:
    first_acc = 0
    second_acc = 0
    with open(file) as f:
        for line in f:
            line = line.split(':')
            total = int(line[0])
            numbers = [int(n) for n in line[1].split()]
            first_dfs = first_part(total, numbers)
            first_acc += first_dfs
            if first_dfs == 0:
                second_dfs = second_part(total, numbers)
                second_acc += second_dfs
    print('First part result:', first_acc)
    print('Second part result:', second_acc + first_acc)


bridge_repair('test2.txt')
