def find_fuels(crabs: list[int]) -> dict[int, int]:
    possibilities = {}
    for pos in crabs:
        possibilities[pos] = 0
        for crab in crabs:
            possibilities[pos] += abs(pos - crab)
    return possibilities


def first_part(crabs: list[int]) -> int:
    fuels = find_fuels(crabs)
    return min(fuels.values())


def second_part(crabs: list[int]) -> int:
    min_fuel = float('inf')
    crabs_seen = set()
    for pos in range(max(crabs)):
        if pos in crabs_seen:
            continue
        possible_fuel = 0
        for crab in crabs:
            fuel = abs(pos - crab)
            possible_fuel += (fuel * (fuel + 1)) // 2
        min_fuel = min(min_fuel, possible_fuel)
    return min_fuel


def parsing(file: str) -> list[int]:
    with open(file) as f:
        return list(map(int, f.read().split(',')))


if __name__ == '__main__':
    crabs = parsing('test2.txt')
    # print('First part result:', first_part(crabs))
    print('Second part result:', second_part(crabs))
