class Map:

    def __init__(self, tiles: list[tuple[int, int]],
                 height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.tiles = sorted(tiles)
        self.tiles_add = set(tiles)
        self.ranges_x = {}
        self.ranges_y = {}

    def first_part(self) -> int:
        max_area = 0
        for x, y in self.tiles:
            for x2, y2 in self.tiles:
                area = (abs(x - x2) + 1) * (abs(y - y2) + 1)
                max_area = max(max_area, area)
        return max_area

    def second_part(self) -> int:
        possible_areas = self.all_area()
        possible_areas_sort = sorted(possible_areas, reverse=True)
        self.ranges_created()
        for area, c1, c2, c3, c4 in possible_areas_sort:
            if c1 not in self.tiles_add:
                if not self.is_inside(c1[0], c1[1]):
                    continue
            if c2 not in self.tiles_add:
                if not self.is_inside(c2[0], c2[1]):
                    continue
            if c3 not in self.tiles_add:
                if not self.is_inside(c3[0], c3[1]):
                    continue
            if c4 not in self.tiles_add:
                if not self.is_inside(c4[0], c4[1]):
                    continue
            return area

    def ranges_created(self) -> None:
        """A refaire"""
        i = 0
        while i < len(self.tiles):
            x = self.tiles[i][0]
            y_start = self.tiles[i][1]
            i += 1
            while i < len(self.tiles) and self.tiles[i][0] == x:
                i += 1
            y_end = self.tiles[i - 1][1]
            self.ranges_x[x] = (y_start, y_end)
        sort_y = sorted(self.tiles, key=lambda x: x[1])
        i = 0
        while i < len(sort_y):
            y = sort_y[i][1]
            x_start = sort_y[i][0]
            i += 1
            while i < len(sort_y) and sort_y[i][1] == y:
                i += 1
            x_end = sort_y[i - 1][0]
            self.ranges_y[y] = (x_start, x_end)

    def is_inside(self, x, y) -> bool:
        min_x, max_x = self.ranges_x[x]
        if min_x > x or x > max_x:
            return False
        min_y, max_y = self.ranges_y[y]
        if min_y > y or y > max_y:
            return False
        return True

    def all_area(self) -> None:
        areas = []
        for i, (x, y) in enumerate(self.tiles):
            for x2, y2 in self.tiles[i + 1:]:
                area = (abs(x - x2) + 1) * (abs(y - y2) + 1)
                coin_1 = (x, y2)
                coin_2 = (x2, y)
                if coin_1 != coin_2 != (x, y) != (x2, y2):
                    areas.append((area, (x, y), (x2, y2), coin_1, coin_2))
        return areas


def parsing(file: str) -> list[tuple[int, int]]:
    tiles: list = []
    with open(file) as f:
        for line in f:
            line_split = line.strip().split(',')
            tiles.append((int(line_split[0]), int(line_split[1])))
    return tiles


if __name__ == '__main__':
    tiles = parsing('test1.txt')
    map1 = Map(tiles, max(tiles, key=lambda x: x[1])[1] + 1, max(tiles)[0] + 1)
    # print("First part result: ", map1.first_part())
    # print("Second part result: ", map1.second_part_map())
    print("Second part result: ", map1.second_part())
