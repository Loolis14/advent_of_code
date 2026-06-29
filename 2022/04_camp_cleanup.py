def first_part(file: str) -> int:
    final_pairs = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            elf_1, elf_2 = line.split(',')
            start1, end1 = tuple(map(int, elf_1.split('-')))
            start2, end2 = tuple(map(int, elf_2.split('-')))
            if start1 >= start2 and end1 <= end2 or start2 >= start1 and end2 <= end1:
                final_pairs += 1
    return final_pairs


def second_part(file: str) -> int:
    nb_pair_in_commun = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            elf_1, elf_2 = line.split(',')
            start1, end1 = tuple(map(int, elf_1.split('-')))
            start2, end2 = tuple(map(int, elf_2.split('-')))
            if end1 >= start2 and start2 >= start1 or end2 >= start1 and start1 >= start2:
                nb_pair_in_commun += 1
    return nb_pair_in_commun


# print('First part:', first_part('test1.txt'))
print('Second part:', second_part('test2.txt'))
