def f(a, n):
    s = 0
    while a > 0:
        s += a % n
        a = a // n
    return s == 75

for n in range(2, 100):
    if f(n ** 25 - 2 * n ** 13 + 10, n):
        print(n)
        break
