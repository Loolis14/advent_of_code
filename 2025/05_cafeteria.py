def second_part(fresh_id_range: list[tuple[int, int]]) -> int:
    fresh = 0
    for low, high in fresh_id_range:
        fresh += high - low + 1
    return fresh


def first_part() -> int:
    with open('test2.txt') as f:
        content = f.read().splitlines()
        split_index = content.index('')
        fresh_ranges = content[:split_index]
        ingredients_id = content[split_index + 1:]
    fresh_id = []
    for str_range in fresh_ranges:
        low, high = str_range.split('-')
        fresh_id.append((int(low), int(high)))
    fresh_id_sort = sorted(fresh_id)
    fresh_id_range = [fresh_id_sort[0]]
    for low, high in fresh_id_sort[1:]:
        if low <= fresh_id_range[-1][1]:
            last_low, last_high = fresh_id_range.pop()
            fresh_id_range.append((last_low, max(high, last_high)))
        else:
            fresh_id_range.append((low, high))

    print('Second part result: ', second_part(fresh_id_range))

    ingredients_id = sorted(list(map(int, ingredients_id)), reverse=True)
    low, high = fresh_id_range.pop()
    fresh = 0
    i = 0
    while i < len(ingredients_id):
        if ingredients_id[i] > high:
            i += 1
        else:
            if ingredients_id[i] >= low:
                fresh += 1
                i += 1
            else:
                if fresh_id_range:
                    low, high = fresh_id_range.pop()
                else:
                    break
    return fresh


print('First part result: ', first_part())
