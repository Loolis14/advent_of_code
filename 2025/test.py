# Memoization: dictionnaire qui va memoriser les éléments que tu as deja eu
cache = {1: 1, 2: 1}


def fibonnaci(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonnaci(n - 1) + fibonnaci(n - 2)
        return cache[n]


print(fibonnaci(10))
print(cache)
