def first_part(file: str) -> int:
    max_carrying = 0
    with open(file) as f:
        current_elf_carrying = 0
        for line in f:
            line = line.rstrip('\n')
            if line:
                current_elf_carrying += int(line)
            else:
                max_carrying = max(current_elf_carrying, max_carrying)
                current_elf_carrying = 0
        max_carrying = max(current_elf_carrying, max_carrying)
    return max_carrying


def second_part(file: str) -> int:
    elves_carrying = []
    with open(file) as f:
        current_elf_carrying = 0
        for line in f:
            line = line.rstrip('\n')
            if line:
                current_elf_carrying += int(line)
            else:
                elves_carrying.append(current_elf_carrying)
                current_elf_carrying = 0
        if current_elf_carrying > 0:
            elves_carrying.append(current_elf_carrying)
    return sum(sorted(elves_carrying, reverse=True)[:3])


# print('First part solution:', first_part('test2.txt'))
print('Second part solution:', second_part('test2.txt'))
