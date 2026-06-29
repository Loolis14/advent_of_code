# My first approach but doesn't work with a lot of datas.

class Map:

    def __init__(self, tiles: list[tuple[int, int]],
                 height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.tiles_original = tiles
        self.tiles_add = set(tiles)

    def first_part(self) -> int:
        max_area = 0
        for x, y in self.tiles_original:
            for x2, y2 in self.tiles_original:
                area = (abs(x - x2) + 1) * (abs(y - y2) + 1)
                max_area = max(max_area, area)
        return max_area

    def second_part_set(self) -> int:
        self.possible_abscissa()
        self.possible_ordinate()
        return self.find_max_area()

    def possible_abscissa(self) -> None:
        tiles_sort = sorted(self.tiles_original, key=lambda x: (x[1], x[0]))
        i = 0
        while i < len(tiles_sort):
            y = tiles_sort[i][1]
            x_start = tiles_sort[i][0]
            i += 1
            while i < len(tiles_sort) and tiles_sort[i][1] == y:
                i += 1
            x_end = tiles_sort[i - 1][0]
            for x in range(x_start, x_end):
                self.tiles_add.add((x, y))

    def possible_ordinate(self) -> None:
        tiles = list(self.tiles_add)
        tiles_sort = sorted(tiles, key=lambda x: (x[0], x[1]))
        i = 0
        while i < len(tiles_sort):
            x = tiles_sort[i][0]
            y_start = tiles_sort[i][1]
            i += 1
            while i < len(tiles_sort) and tiles_sort[i][0] == x:
                i += 1
            y_end = tiles_sort[i - 1][1]
            for y in range(y_start, y_end):
                self.tiles_add.add((x, y))

    def second_part_map(self) -> int:
        self.map = [['#' if (j, i) in tiles else '.'
                     for j in range(self.width)] for i in range(self.height)]
        self.fill_abscissa()
        self.fill_ordinate()
        return self.find_max_area()

    def fill_abscissa(self) -> None:
        for y_line, line in enumerate(self.map):
            if line.count('#') < 2:
                continue
            left = line.index('#')
            right = ''.join(line).rindex('#')
            for i in range(left, right):
                line[i] = '#'
                self.tiles_add.add((i, y_line))

    def fill_ordinate(self) -> None:
        tiles_sort = sorted(sorted(list(self.tiles_add), key=lambda x: x[1]),
                            key=lambda x: x[0])
        hashtag_bornes = {}
        stack = []
        for x, y in tiles_sort:
            if not stack:
                stack.append((x, y))
            else:
                if stack[-1][0] == x:
                    stack.append((x, y))
                else:
                    x_line = stack[-1][0]
                    hashtag_bornes.setdefault(x_line, 0)
                    start = self.width
                    end = 0
                    while stack:
                        new_x, new_y = stack.pop()
                        start = min(start, new_y)
                        end = max(end, new_y)
                    hashtag_bornes[x_line] = (start, end)
                    stack.append((x, y))
        if stack:
            x_line = stack[-1][0]
            hashtag_bornes.setdefault(x_line, 0)
            start = self.width
            end = 0
            while stack:
                new_x, new_y = stack.pop()
                start = min(start, new_y)
                end = max(end, new_y)
            hashtag_bornes[x_line] = (start, end)
        for index_x, indexes_y in hashtag_bornes.items():
            for i in range(indexes_y[0], indexes_y[1]):
                self.map[i][index_x] = '#'
                self.tiles_add.add((index_x, i))

    def find_max_area(self) -> int:
        max_area = 0
        for x, y in tiles:
            for x2, y2 in tiles[1:]:
                coin_1 = (x, y2)
                coin_2 = (x2, y)
                if coin_2 in self.tiles_add and coin_1 in self.tiles_add:
                    area = (abs(x - x2) + 1) * (abs(y - y2) + 1)
                    max_area = max(max_area, area)
        return max_area


def parsing(file: str) -> list[tuple[int, int]]:
    tiles: list = []
    with open(file) as f:
        for line in f:
            line_split = line.strip().split(',')
            tiles.append((int(line_split[0]), int(line_split[1])))
    return tiles


if __name__ == '__main__':
    tiles = parsing('test2.txt')
    map1 = Map(tiles, max(tiles, key=lambda x: x[1])[1] + 1, max(tiles)[0] + 1)
    # print("First part result: ", map1.first_part())
    # print("Second part result: ", map1.second_part_map())
    print("Second part result: ", map1.second_part_set())
