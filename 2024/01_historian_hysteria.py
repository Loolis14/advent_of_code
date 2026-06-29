from collections import Counter


def second_part(column_1: list[int], column_2: list[int]) -> int:
    number_count = Counter(column_2)
    similarity_score = 0
    for n in column_1:
        similarity_score += n * number_count[n]
    return similarity_score


def first_part(file: str) -> int:
    column_1 = []
    column_2 = []
    with open(file) as f:
        for line in f:
            numbers = line.split()
            column_1.append(int(numbers[0]))
            column_2.append(int(numbers[1]))
    print('Second part solution is:', second_part(column_1, column_2))
    column_1, column_2 = sorted(column_1), sorted(column_2)
    distance = 0
    for association in zip(column_1, column_2):
        a, b = association
        distance += abs(a - b)
    return distance


print('First part solution is:', first_part('test2.txt'))


"""
First Version, december 2024

a = open("input_1.txt").read()
pair = []
impair = []

for v,n in enumerate(a.split()):
    if v%2 == 0:
        pair.append(int(n))
    else:
        impair.append(int(n))

pair = sorted(pair)
impair = sorted(impair)
difference = 0
for i,c in enumerate(pair):
    difference+= abs(c-impair[i])
print(difference) #part 1 : 1666427

score=0
for c in pair:
    h_m = impair.count(c)
    score += h_m * c

print(score) #part 2 : 24316233
"""
