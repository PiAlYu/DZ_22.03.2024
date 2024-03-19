from math import ceil
from functools import lru_cache

@lru_cache(None)
def f(n, h):
    if n == 1: return h % 2
    if h % 2 == 0:
        return any(f(i, h + 1) for i in range(ceil(n / 2), n))
    return all(f(i, h + 1) for i in range(ceil(n / 2), n))

k = 0
for j in range(100, 1000):
    if f(j, 0) == 1:
        k += 1
print(k)
