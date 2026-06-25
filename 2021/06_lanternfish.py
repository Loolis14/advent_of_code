from functools import lru_cache


def first_part(fishes: list[int]) -> int:
    n_count = 0

    def count_fish(loop_left: int, fishes: list[int]):
        if loop_left == 0:
            return len(fishes)
        new_fishes = []
        fish_add = 0
        for fish in fishes:
            if fish == 0:
                new_fishes.append(6)
                fish_add += 1
            else:
                new_fishes.append(fish - 1)
        for _ in range(fish_add):
            new_fishes.append(8)
        return count_fish(loop_left - 1, new_fishes)

    for fish in fishes:
        n_count += count_fish(80, [fish])
    return n_count


def first_part_lru(fishes: list[int]) -> int:
    n_count = 0

    @lru_cache(maxsize=None)
    def count_fish(loop_left: int, fish: int):
        if loop_left == 0:
            return 1
        if fish == 0:
            return count_fish(loop_left - 1, 8) + count_fish(loop_left - 1, 6)
        return count_fish(loop_left - 1, fish - 1)

    for fish in fishes:
        n_count += count_fish(256, fish)
    return n_count


def parsing(file: str) -> list[int]:
    with open(file) as f:
        return list(map(int, f.read().split(',')))


if __name__ == '__main__':
    fishes = parsing('test2.txt')
    print('First part result:', first_part_lru(fishes))
