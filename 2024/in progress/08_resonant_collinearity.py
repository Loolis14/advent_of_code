# A faire
def first_part(file) -> None:
    antenna = []
    with open(file) as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            for j, c in enumerate(line):
                if c != '.':
                    antenna.append((c, j, i))
    print(antenna)


print('First part result:', first_part('test1.txt'))
# print('Second part result:', second_acc + first_acc)
