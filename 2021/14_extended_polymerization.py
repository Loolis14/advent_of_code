from collections import Counter


def parsing(file: str) -> tuple:
    with open(file) as f:
        content = f.read().splitlines()
        polymere = content[0]
        rules = {s[:2]: s[-1] for s in content[2:]}
    return polymere, rules


def first_part(polymere: str, rules: dict[str, str]) -> int:
    for i in range(10):
        new_polymere = ''
        for i, c in enumerate(polymere):
            if i == 0:
                new_polymere += c
                continue
            pair = new_polymere[-1] + c
            new_polymere += rules[pair] + c
        polymere = new_polymere
    occurences = Counter(polymere)
    return max(occurences.values()) - min(occurences.values())


if __name__ == '__main__':
    polymere, rules = parsing('test1.txt')
    print('First part result:', first_part(polymere, rules))
