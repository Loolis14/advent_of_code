# IN PROGRESS. There is probably something I don't under on the assignement
# distance : somme des 3 squares

def calcul_min_distance(
        points: list[tuple[int, int, int]]
        ) -> list[tuple[int, int]]:
    distances = {}
    for i, (x1, y1, z1) in enumerate(points):
        distances[i] = (float('inf'), 0)
        for j, (x2, y2, z2) in enumerate(points[i + 1:]):
            distance = (
                ((x2 - x1) ** 2 +
                 (y2 - y1) ** 2 +
                 (z2 - z1) ** 2) ** 0.5)
            min_distance = min(distances[i][0], distance)
            if min_distance == distance:
                distances[i] = (min_distance, j + i + 1)
    connection_to_made = []
    for index_a, (d, index_b) in distances.items():
        connection_to_made.append((index_a, index_b))
    return connection_to_made


def first_part(file: str) -> list[set]:
    points = parsing(file)
    connections_to_make = calcul_min_distance(points)
    circuit_made: list[set] = []
    for point1, point2 in connections_to_make:
        connection_made = False
        for circuit in circuit_made:
            if point1 in circuit or point2 in circuit:
                circuit.add(point1)
                circuit.add(point2)
                connection_made = True
                break
        if not connection_made:
            circuit_made.append({point1, point2})
    return circuit_made


def parsing(file: str) -> list[tuple[int, int, int]]:
    points = []
    with open(file) as f:
        for line in f:
            line = line.strip('\n')
            x, y, z = map(int, line.split(','))
            points.append((x, y, z))
    return points


print('First part:', first_part('test1.txt'))
