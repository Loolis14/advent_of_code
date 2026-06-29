def second_part(directory_sizes: dict[str, int]) -> int:
    pc_used_place = directory_sizes[("/",)]
    total_amount_used_space = 70000000 - pc_used_place
    need_for_update = 30000000 - total_amount_used_space
    return min(n for n in directory_sizes.values() if n > need_for_update)


def first_part(file: str) -> int:
    curr_dir = []
    dir_sizes = {}
    with open(file) as f:
        for line in f:
            cmd = line.rstrip().split()
            if cmd[0] == '$' and cmd[1] == 'cd':
                if cmd[2] == '..':
                    curr_dir.pop()
                else:
                    curr_dir.append(cmd[2])
                continue
            if cmd[0].isdigit():
                for i, dir in enumerate(curr_dir):
                    path = tuple(curr_dir[:i + 1])
                    dir_sizes[path] = dir_sizes.get(path, 0) + int(cmd[0])
    print('Second part solution:', second_part(dir_sizes))
    return sum(size for size in dir_sizes.values() if size <= 100000)


print('First part :', first_part('test2.txt'))
