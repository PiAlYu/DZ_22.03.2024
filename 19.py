from math import ceil

def f(n, h):
    if h == 5 and n == 1: return True
    if n == 1: return False
    if h % 2 == 0:
        return any(f(i, h + 1) for i in range(ceil(n / 2), n))
    return all(f(i, h + 1) for i in range(ceil(n / 2), n))

k = 0
for j in range(100, 2, -1):
    if f(j, 0):
        print(j)
        break
