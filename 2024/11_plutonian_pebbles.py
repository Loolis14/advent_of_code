from functools import lru_cache


def first_part(file: str) -> None:
    with open(file) as f:
        content = f.readline().split()
    for _ in range(25):
        split = False
        for i, n in enumerate(content):
            if split:
                split = False
                continue
            if n == '0':
                content[i] = '1'
            elif len(n) % 2 == 0:
                content[i] = n[:len(n) // 2]
                second_number = n[len(n) // 2:]
                content.insert(i + 1, str(int(second_number)))
                split = True
            else:
                content[i] = str(int(n) * 2024)
    return len(content)


def second_part(file: str) -> int:
    with open(file) as f:
        content = list(map(int, f.readline().split()))

    @lru_cache(maxsize=None)
    def count_stones(number: int, loop_left: int):
        if loop_left == 0:
            return 1
        if number == 0:
            return count_stones(1, loop_left - 1)
        n_str = str(number)
        if len(n_str) % 2 == 0:
            n1 = int(n_str[:len(n_str) // 2])
            n2 = int(n_str[len(n_str) // 2:])
            return (count_stones(n1, loop_left - 1) +
                    count_stones(n2, loop_left - 1))
        else:
            return count_stones(number * 2024, loop_left - 1)
    return sum(count_stones(n, 75) for n in content)


# print('First part result:', first_part('test1.txt'))
print('Second part result:', second_part('test2.txt'))

"""
First Version, december 2024

test = "64554 35 906 6 6960985 5755 975820 0"
l = []
for number in test.split():
    l.append(number)

def blink(l):
    sol = []
    for n in l:
        if n == "0" or n == 0 :
            sol.append(1)
        elif len(str(n)) % 2 == 0:
            x = len(str(n))//2
            n = str(n)
            sol.append(int(n[:x]))
            sol.append(int(n[x:]))
        else:
            sol.append(int(n)*2024)
    return sol
a = blink(l)
b = blink(a)
c = blink(b)
d = blink(c)
e = blink(d)
f = blink(e)
g = blink(f)
h = blink(g)
i = blink(h)
j = blink(i)
k = blink(j)
l = blink(k)
m = blink(l)
n = blink(m)
o = blink(n)
p = blink(o)
q = blink(p)
r = blink(q)
s = blink(r)
t = blink(s)
s = blink(t)
u = blink(s)
v = blink(u)
w = blink(v)
x = blink(w)

print(len(x))
"""
