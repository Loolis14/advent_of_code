def second_part(ways: str, direction: dict[str, int]) -> int:
    position_santa = (0, 0)
    position_ia_santa = (0, 0)
    house_visited = {position_santa}
    for i, way in enumerate(ways):
        dx, dy = direction[way]
        if i % 2:
            position_ia_santa = (position_ia_santa[0] + dx,
                                 position_ia_santa[1] + dy)
        else:
            position_santa = (position_santa[0] + dx,
                              position_santa[1] + dy)
        house_visited.add(position_santa)
        house_visited.add(position_ia_santa)
    return len(house_visited)


def first_part(file) -> int:
    present_given = 1
    with open(file) as f:
        ways = f.read()
        position = (0, 0)
        house_visited = {position}
        direction = {'^': (0, -1), 'v': (0, 1),
                     '>': (1, 0), '<': (-1, 0)}
        for way in ways:
            dx, dy = direction[way]
            position = (position[0] + dx, position[1] + dy)
            if position not in house_visited:
                present_given += 1
                house_visited.add(position)
    print('Second part result:', second_part(ways, direction))
    return present_given


print('First part result:', first_part('test2.txt'))
