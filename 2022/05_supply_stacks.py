import re


def find_index(cranes: str) -> list[int]:
    indexes = []
    for i, c in enumerate(cranes):
        if c.isdigit():
            indexes.append(i)
    return indexes


def create_stack(cranes: list[str]) -> list[list[str]]:
    stack_indexes = find_index(cranes[-1])
    cargo_crane = [[] for i in range(len(stack_indexes))]
    for crane in cranes[-2::-1]:
        for i, c in enumerate(crane):
            if c.isalpha():
                cargo_crane[stack_indexes.index(i)].append(c)
    return cargo_crane


def first_part(file: str) -> str:
    with open(file) as f:
        cranes = []
        for line in f:
            line = line.rstrip()
            if not line:
                break
            cranes.append(line)
        cargo_crane = create_stack(cranes)
        for move in f:
            nb, from_, to_ = map(int, re.findall(r'\d+', move))
            for _ in range(nb):
                crane = cargo_crane[from_ - 1].pop()
                cargo_crane[to_ - 1].append(crane)
    return ''.join(crane[-1] for crane in cargo_crane)


def second_part(file: str) -> str:
    with open(file) as f:
        cranes = []
        for line in f:
            line = line.rstrip()
            if not line:
                break
            cranes.append(line)
        cargo_crane = create_stack(cranes)
        for move in f:
            nb, from_, to_ = map(int, re.findall(r'\d+', move))
            crane_to_move = cargo_crane[from_ - 1][- nb:]
            cargo_crane[from_ - 1] = cargo_crane[from_ - 1][:- nb]
            cargo_crane[to_ - 1].extend(crane_to_move)
    return ''.join(crane[-1] for crane in cargo_crane)


if __name__ == '__main__':
    # print('First part:', first_part('test2.txt'))
    print('Second part:', second_part('test2.txt'))
