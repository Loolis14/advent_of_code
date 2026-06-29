# Look at the Gaussian elimination adapted to XOR operations.
import re


def parsing_diagram(diagram: str) -> dict[int, int]:
    light_diagram = {}
    for i, c in enumerate(diagram):
        if c == '.':
            light_diagram[str(i)] = 0
        else:
            light_diagram[str(i)] = 1
    return light_diagram


def parsing_buttons(buttons_str: str) -> list[set[int]]:
    buttons = []
    for word in buttons_str:
        pattern = re.findall(r'\d+', word)
        buttons.append(set(pattern))
    return buttons


def first_part(file: str) -> None:
    with open(file) as f:
        for line in f:
            line_split = line.split()
            light_diagram = parsing_diagram(line_split[0][1:-1])
            buttons = parsing_buttons(line_split[1:-1])
            joltage_requirments = line_split[-1]
            print(buttons)
            break

print('First part result: ', first_part('test1.txt'))
