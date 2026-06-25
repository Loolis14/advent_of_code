class Farm:

    def __init__(self) -> None:
        self.all_gardens: dict[str, set[tuple[int, int]]] = {}
        self.gardens: list[set[tuple[int]]] = []
        self.position_left: set[tuple[int, int]] = set()
        self.width: int = 0
        self.height: int = 0

    def number_adjacent_cells(self, cell: tuple[int, int],
                              cells: list[tuple[int, int]]) -> int:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = cell
        num = 0
        for dx, dy in direction:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in cells:
                num += 1
        return num

    def calculate_perimeter_1(self, cells: list[tuple[int, int]]) -> int:
        perimeter = 4 * len(cells)
        for cell in cells:
            perimeter -= self.number_adjacent_cells(cell, cells)
        return perimeter

    def ext_coin(self, x: int, y: int, cells: set[tuple[int, int]]) -> int:
        coins = 0
        adjacent = {'N': (x, y - 1),
                    'S': (x, y + 1),
                    'E': (x + 1, y),
                    'W': (x - 1, y)}
        if adjacent['N'] not in cells and adjacent['W'] not in cells:
            coins += 1
        if adjacent['N'] not in cells and adjacent['E'] not in cells:
            coins += 1
        if adjacent['S'] not in cells and adjacent['W'] not in cells:
            coins += 1
        if adjacent['S'] not in cells and adjacent['E'] not in cells:
            coins += 1
        return coins

    def int_coin(self, x: int, y: int, cells: set[tuple[int, int]]) -> int:
        coins = 0
        adjacent = {'E': (x + 1, y), 'W': (x - 1, y),
                    'N': (x, y - 1), 'S': (x, y + 1)}
        diagonal = {
            'NW': (x - 1, y - 1),
            'SW': (x - 1, y + 1),
            'NE': (x + 1, y - 1),
            'SE': (x + 1, y + 1)
        }
        if adjacent['W'] not in cells and adjacent['N'] in cells and diagonal['NW'] in cells:
            coins += 1
        if adjacent['W'] not in cells and adjacent['S'] in cells and diagonal['SW'] in cells:
            coins += 1
        if adjacent['E'] not in cells and adjacent['N'] in cells and diagonal['NE'] in cells:
            coins += 1
        if adjacent['E'] not in cells and adjacent['S'] in cells and diagonal['SE'] in cells:
            coins += 1
        return coins

    def calculate_perimeter_2(self, cells: set[tuple[int, int]]) -> int:
        cells_to_check = sorted(list(cells))
        perimeter = 0
        for x, y in cells_to_check:
            perimeter += self.ext_coin(x, y, cells)
            perimeter += self.int_coin(x, y, cells)
        return perimeter

    def parsing_gardens(self, part: int) -> int:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        price = 0
        for garden in self.gardens:
            while garden:
                current_cell = min(garden)
                cells_visited = {current_cell}
                path = [current_cell]
                while path:
                    x, y = path.pop()
                    for dx, dy in direction:
                        new_x, new_y = x + dx, y + dy
                        if (new_x, new_y) in garden and (new_x, new_y) not in cells_visited:
                            path.append((new_x, new_y))
                            cells_visited.add((new_x, new_y))
                area = len(cells_visited)
                if part == 1:
                    perimeter = self.calculate_perimeter_1(list(cells_visited))
                else:
                    perimeter = self.calculate_perimeter_2(cells_visited)
                price += area * perimeter
                garden -= cells_visited
        return price

    def parsing(self, file: str) -> None:
        with open(file) as f:
            for i, line in enumerate(f):
                line = line.strip('\n')
                for j, c in enumerate(line):
                    self.all_gardens.setdefault(c, set()).add((j, i))
        self.width = j
        self.height = i
        self.position_left = set((j, i) for i in range(self.height + 1)
                                 for j in range(self.width + 1))
        self.gardens = self.all_gardens.values()


if __name__ == '__main__':
    p1 = Farm()
    p1.parsing('test2.txt')
    print('First part result:', p1.parsing_gardens(1))
    print('Second part result:', p1.parsing_gardens(2))
