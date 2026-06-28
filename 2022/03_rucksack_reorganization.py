from string import ascii_letters


def first_part(file: str) -> int:
    priorities_items_sum = 0
    with open(file) as f:
        for line in f:
            line = line.strip('\n')
            backpack1, backpack2 = set(line[:len(line) // 2]), set(line[len(line) // 2:])
            letters_in_common = backpack1 & backpack2
            for letter in letters_in_common:
                priorities_items_sum += ascii_letters.index(letter) + 1
    return priorities_items_sum


def second_part(file: str) -> int:
    badges_sum = 0
    with open(file) as f:
        while True:
            groups = [f.readline().rstrip('\n') for i in range(3)]
            if not any(groups):
                break
            letter_in_common = set(groups[0])
            for group in groups[1:]:
                letter_in_common = letter_in_common & set(group)
            badges_sum += ascii_letters.index(list(letter_in_common)[0]) + 1
    return badges_sum


# print('First part result:', first_part('test2.txt'))
print('Second part result:', second_part('test2.txt'))
