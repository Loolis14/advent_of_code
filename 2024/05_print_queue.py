def parsing_rules(order_rules) -> dict[int, set[int]]:
    rules_sort = sorted(order_rules)
    rules: dict[set] = {}
    for a, b in rules_sort:
        rules.setdefault(a, set()).add(b)
    return rules


def is_order(update: list[int], rules: dict[int, set[int]]) -> bool:
    stack = [update[0]]
    for i, n in enumerate(update[1:], start=1):
        if n not in rules:
            stack.append(n)
            continue
        n_rules = rules[n]
        for previous in stack:
            if previous in n_rules:
                return False
        stack.append(n)
    return True


def second_part(updates: list[int],
                rules: dict[int, set[int]]) -> int:
    middle_page_sum = 0
    for update in updates:
        update_sort = []
        stack = []
        i = 0
        while len(update_sort) < len(update):
            if not update_sort:
                update_sort.append(update[i])
                i += 1
            if i < len(update) and update[i] not in rules:
                update_sort.append(update[i])
                i += 1
            elif i < len(update) and update_sort[-1] not in rules[update[i]]:
                update_sort.append(update[i])
                i += 1
            else:
                while update_sort and update_sort[-1] in rules[update[i]]:
                    after = update_sort.pop()
                    stack.append(after)
                update_sort.append(update[i])
                i += 1
                while stack:
                    add = stack.pop()
                    update_sort.append(add)
        middle_update = (len(update) // 2 if len(update) % 2
                         else len(update) // 2 - 1)
        middle_page_sum += update_sort[middle_update]
    return middle_page_sum


def first_part(file: str) -> int:
    order_rules = []
    updates = []
    with open(file) as f:
        second_half = False
        for line in f:
            if line == '\n':
                second_half = True
                continue
            if not second_half:
                line = line.strip('\n')
                order_rules.append(tuple(map(int, line.split('|'))))
            else:
                temp = []
                for n in line.split(','):
                    n = n.strip('\n')
                    temp.append(int(n))
                updates.append(temp)
    rules = parsing_rules(order_rules)
    middle_page_sum = 0
    update_to_sort = []
    for update in updates:
        if is_order(update, rules):
            middle_update = (len(update) // 2 if len(update) % 2
                             else len(update) // 2 - 1)
            middle_page_sum += update[middle_update]
        else:
            update_to_sort.append(update)
    print('Second part solution:',
          second_part(update_to_sort, rules))
    return middle_page_sum


print('First part solution:', first_part('test2.txt'))

"""
First Version, december 2024

import re
test = open("input_5_pair.txt").read().splitlines()
l = open("input_5_list.txt").read().splitlines()

regex = re.compile(r'(\d+)(\|)(\d+)')

non = []
for list in l:
    d={}
    for i,n in enumerate(list.split(",")):
        d[str(n)] = i

    for match in test:
        m = regex.search(match)
        a,op,b = m.groups()
        if a not in d or b not in d:
            continue
        elif d[str(a)] < d[str(b)]:
            continue
        else:
            non.append(list)
            break
oui = []
for el in l:
    if el not in non:
        oui.append(el)

acc = 0
for l3 in oui:
    x = 0
    oui2 = []
    for n in l3.split(","):
        x += 1
        oui2.append(n)
    y = x//2

    acc += int(oui2[y])

print(acc)
"""
