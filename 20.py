def f(n, h):
    if n == 1: return h % 2
    if h % 2 == 0:
        return all(f(i, h + 1) for i in range(n // 2, n))
    return any(f(i, h + 1) for i in range(n // 2, n))

k = 0
for j in range(2, 100):
    if f(j, 0) == 1:
        k += 1
print(k)
