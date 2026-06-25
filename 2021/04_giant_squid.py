class Bingo:
    bingos: list['Bingo'] = []
    bingo_wins: set['Bingo'] = set()

    def __init__(self, grid: list[list[str]]) -> None:
        self.grid: list[list[str]] = grid
        self.width: int = len(self.grid[0])
        self.height: int = len(self.grid)

    def is_winner_row(self) -> bool:
        for row in self.grid:
            if row.count(True) == 5:
                return True
        return False

    def is_winner_column(self) -> bool:
        i = 0
        while i < self.width:
            j = 0
            while j < self.height:
                if isinstance(self.grid[j][i], bool):
                    j += 1
                else:
                    break
            if j == self.height:
                return True
            i += 1
        return False

    def first_check_numbers(self, numbers: set[str]) -> None:
        for y, row in enumerate(self.grid):
            for x, c in enumerate(row):
                if c in numbers:
                    self.grid[y][x] = True

    def check_numbers(self, numbers: int) -> None:
        for y, row in enumerate(self.grid):
            for x, c in enumerate(row):
                if c == numbers:
                    self.grid[y][x] = True

    def sum_numbers_left(self) -> int:
        acc = 0
        for row in self.grid:
            for c in row:
                if isinstance(c, str):
                    acc += int(c)
        return acc

    @classmethod
    def first_part(cls, number_call: list[int]) -> int:
        for bingo in cls.bingos:
            bingo.first_check_numbers(set(number_call[:5]))
            if bingo.is_winner_row() or bingo.is_winner_column():
                return bingo.sum_numbers_left() * int(number_call[:5])
        i = 5
        while True:
            number_to_call = number_call[i]
            for bingo in cls.bingos:
                bingo.check_numbers(number_to_call)
                if bingo.is_winner_row() or bingo.is_winner_column():
                    return bingo.sum_numbers_left() * int(number_to_call)
            i += 1

    @classmethod
    def second_part(cls, number_call: list[int]) -> int:
        for bingo in cls.bingos:
            bingo.first_check_numbers(set(number_call[:5]))
            if bingo.is_winner_row() or bingo.is_winner_column():
                cls.bingo_wins.add(bingo)
        i = 5
        while True:
            number_to_call = number_call[i]
            for bingo in cls.bingos:
                if bingo in cls.bingo_wins:
                    continue
                bingo.check_numbers(number_to_call)
                if bingo.is_winner_row() or bingo.is_winner_column():
                    cls.bingo_wins.add(bingo)
                    if len(cls.bingo_wins) == len(cls.bingos):
                        return bingo.sum_numbers_left() * int(number_to_call)
            i += 1


def parsing(file: str) -> list[int]:
    with open(file) as f:
        temp_bingo = []
        for i, line in enumerate(f):
            line = line.strip('\n')
            if i == 0:
                number_call = line.split(',')
                continue
            if i == 1:
                continue
            if not line:
                b1 = Bingo(temp_bingo)
                Bingo.bingos.append(b1)
                temp_bingo = []
            else:
                temp_bingo.append(line.split())
        b1 = Bingo(temp_bingo)
        Bingo.bingos.append(b1)
    return number_call


if __name__ == '__main__':
    number_call = parsing('test2.txt')
    # print('First part result:', Bingo.first_part(number_call))
    print('Second part result:', Bingo.second_part(number_call))
