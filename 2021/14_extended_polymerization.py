from collections import Counter


def parsing(file: str) -> tuple:
    with open(file) as f:
        content = f.read().splitlines()
        polymere = content[0]
        rules = {s[:2]: s[-1] for s in content[2:]}
    return polymere, rules


def second_part(polymere: str, rules: dict[str, str]) -> int:
    paires_occurences = {}
    letters_occurences = {}
    for i, c in enumerate(polymere):
        if i == 0:
            continue
        pair = polymere[i - 1] + c
        letters_occurences[c] = letters_occurences.get(c, 0) + 1
        letters_occurences[polymere[i - 1]] = letters_occurences.get(polymere[i - 1], 0) + 1
        paires_occurences[pair] = paires_occurences.get(pair, 0) + 1
    for i in range(10):
        new_pairs = []
        for current_pair, nb in paires_occurences.items():
            letter_between = rules[current_pair]
            letters_occurences[letter_between] = letters_occurences.get(letter_between, 0) + 2 * nb
            new_pairs.append((current_pair[0] + letter_between))
            new_pairs.append((letter_between + current_pair[1]))
            paires_occurences[current_pair] = 0
        for pair, nb in new_pairs:
            paires_occurences[pair] = nb
        print(letters_occurences)
    print(paires_occurences)


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
    print(occurences)
    return max(occurences.values()) - min(occurences.values())


if __name__ == '__main__':
    polymere, rules = parsing('test1.txt')
    print('First part result:', second_part(polymere, rules))
