def first_part(file: str) -> int:
    with open(file) as f:
        content = f.read().splitlines()
        grid = [[int(c) for c in s]for s in content]
    grid_width = len(grid[0])
    grid_height = len(grid)
    low_points = []
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for y, line in enumerate(grid):
        for x, n in enumerate(line):
            neighbours = []
            for dx, dy in direction:
                neighbour_x, neighbour_y = x + dx, y + dy
                if (0 <= neighbour_x < grid_width and
                        0 <= neighbour_y < grid_height):
                    neighbours.append(grid[neighbour_y][neighbour_x])
            bigger = False
            for neighbour in neighbours:
                if n >= neighbour:
                    bigger = True
            if not bigger:
                low_points.append(n)
    return sum(1 + point for point in low_points)


def is_low(n: int, x: int, y: int, grid: list[list[int]]) -> bool:
    neighbours = find_neighbours(grid, x, y)
    bigger = False
    for neighbour in neighbours:
        if n >= neighbour[0]:
            bigger = True
    return not bigger


def find_neighbours(grid: list[list[int]],
                    x: int, y: int) -> list[tuple[int, int, int]]:
    width = len(grid[0])
    height = len(grid)
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    neighbours = []
    for dx, dy in direction:
        ngbr_x, ngbr_y = x + dx, y + dy
        if 0 <= ngbr_x < width and 0 <= ngbr_y < height:
            neighbours.append((grid[ngbr_y][ngbr_x], ngbr_x, ngbr_y))
    return neighbours


def search_basin(grid: list[list[int]], x: int, y: int, seen: set) -> int:
    queue = [(x, y)]
    basin_width = 0
    while queue:
        curr_x, curr_y = queue.pop()
        neighbours = find_neighbours(grid, curr_x, curr_y)
        for neighbour in neighbours:
            ngbr_n, ngbr_x, ngbr_y = neighbour
            if ngbr_n == 9 or (ngbr_x, ngbr_y) in seen:
                continue
            queue.append((ngbr_x, ngbr_y))
            basin_width += 1
            seen.add((ngbr_x, ngbr_y))
    return basin_width, seen


def second_part(file: str) -> int:
    with open(file) as f:
        content = f.read().splitlines()
        grid = [[int(c) for c in s]for s in content]
    size_basins = []
    seen = set()
    for y, line in enumerate(grid):
        for x, n in enumerate(line):
            if is_low(n, x, y, grid):
                size, new_seen = search_basin(grid, x, y, seen)
                size_basins.append(size)
                seen.update(new_seen)
    size_basins.sort()
    return size_basins[-1] * size_basins[-2] * size_basins[-3]


# print('First part result:', first_part('test2.txt'))
print('First part result:', second_part('test2.txt'))
