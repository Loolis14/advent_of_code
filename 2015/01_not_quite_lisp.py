with open('test1.txt') as f:
    content = f.readline()
    floor = 0
    basement_found = False
    for i, c in enumerate(content):
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1 and not basement_found:
            basement = i + 1
            basement_found = True
    print(f'First part result: {floor}')
    print(f'Second part result: {basement}')
