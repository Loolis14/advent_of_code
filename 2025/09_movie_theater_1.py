# Second approach to run even with a lot of datas for the second part.
# Still not working though. Missing : not have all the width and height.


class Map:

    def __init__(self, tiles: list[tuple[int, int]]) -> None:
        self.tiles = sorted(tiles)
        self.tiles_set = set(tiles)
        self.width = max(x for x, y in tiles) + 1 if tiles else 0
        self.height = max(y for x, y in tiles) + 1 if tiles else 0

    def first_part(self) -> int:
        max_area = 0
        for x, y in self.tiles:
            for x2, y2 in self.tiles:
                area = (abs(x - x2) + 1) * (abs(y - y2) + 1)
                max_area = max(max_area, area)
        return max_area

    def second_part(self) -> int:
        max_area: int = 0
        h = [0] * self.width
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.tiles_set:
                    h[x] += 1
                else:
                    h[x] = 0
            max_area = max(max_area, self.monotonic_stack(h))
        return max_area

    def monotonic_stack(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        p = 0
        while p < len(heights):
            if not stack or heights[p] >= heights[stack[-1]]:
                stack.append(p)
                p += 1
            else:
                top = stack.pop()
                width = p if not stack else p - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)

        while stack:
            top = stack.pop()
            width = p if not stack else p - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)
        return max_area


def parsing(file: str) -> list[tuple[int, int]]:
    tiles: list = []
    with open(file) as f:
        for line in f:
            line_split = line.strip().split(',')
            tiles.append((int(line_split[0]), int(line_split[1])))
    return tiles


if __name__ == '__main__':
    tiles = parsing('test1.txt')
    map1 = Map(tiles)
    # print("First part result: ", map1.first_part())
    print("Second part result: ", map1.second_part())
