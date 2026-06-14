# Deuxieme partie a finir

def first_part(file: str) -> int:
    safe_reports = 0
    with open(file) as f:
        for line in f:
            levels = list(map(int, line.split()))
            increasing = False if levels[0] > levels[1] else True
            safe = True
            for i in range(1, len(levels)):
                if increasing and levels[i - 1] >= levels[i]:
                    safe = False
                    break
                if not increasing and levels[i - 1] <= levels[i]:
                    safe = False
                    break
                if abs(levels[i - 1] - levels[i]) > 3:
                    safe = False
                    break
            if safe:
                safe_reports += 1
    return safe_reports


def find_error(levels: list[int]) -> dict[str, int]:
    error_hash = {'inf_0': 0, 'equal': 0, 'sup_0': 0,
                  'too_much': 0, 'index_error': 0}

    for i in range(1, len(levels)):
        number = levels[i - 1] - levels[i]
        if number == 0:
            error_hash['equal'] += 1
            error_hash['index_error'] = i
        elif -3 > number or number > 3:
            error_hash['too_much'] += 1
            error_hash['index_error'] = i
        elif number < 0:
            error_hash['inf_0'] += 1
        elif number > 0:
            error_hash['sup_0'] += 1
    return error_hash


def second_part(file: str) -> int:
    safe_reports = 0
    with open(file) as f:
        for line in f:
            levels = list(map(int, line.split()))
            errors_hash = find_error(levels)
            bad_lvl = (errors_hash['equal'] + errors_hash['too_much']
                       + min(errors_hash['inf_0'], errors_hash['sup_0']))
            if bad_lvl == 0:
                safe_reports += 1
                continue
            elif bad_lvl > 1:
                continue
            elif bad_lvl == 1:
                if errors_hash['equal'] == 1:
                    new_level = [levels[i] for i in range(len(levels))
                                 if i != errors_hash['index_error']]
                    second_chance_hash = find_error(new_level)
                elif errors_hash['inf_0'] == 1:
                    index = 1
                    while index < len(levels):
                        if levels[index - 1] > levels[index]:
                            break
                        index += 1
                    new_level = [levels[i] for i in range(len(levels))
                                 if i != index]
                    second_chance_hash = find_error(new_level)
                elif errors_hash['sup_0'] == 1:
                    index = 1
                    while index < len(levels):
                        if levels[index - 1] > levels[index]:
                            break
                        index += 1
                    new_level = [levels[i] for i in range(len(levels))
                                 if i != index]
                    second_chance_hash = find_error(new_level)
                elif errors_hash['too_much'] == 1:
                    first_case = [levels[i] for i in range(len(levels))
                                  if i != errors_hash['index_error']]
                    second_case = [levels[i] for i in range(len(levels))
                                   if i != errors_hash['index_error'] - 1]
                    second_chance_hash1 = find_error(first_case)
                    second_chance_hash2 = find_error(second_case)
                    second_chance1 = (
                        second_chance_hash1['equal'] +
                        second_chance_hash1['too_much'] +
                        min(second_chance_hash1['inf_0'],
                            second_chance_hash1['sup_0']))
                    second_chance2 = (
                        second_chance_hash2['equal'] +
                        second_chance_hash2['too_much'] +
                        min(second_chance_hash2['inf_0'],
                            second_chance_hash2['sup_0']))
                    if second_chance1 == 0 or second_chance2 == 0:
                        safe_reports += 1
                    continue
                second_chance = (second_chance_hash['equal'] +
                                 second_chance_hash['too_much']
                                 + min(second_chance_hash['inf_0'],
                                       second_chance_hash['sup_0']))
                if second_chance == 0:
                    safe_reports += 1
    return safe_reports


# print('First part solution is:', first_part('test2.txt'))
print('Second part solution is:', second_part('2024/test2.txt'))
