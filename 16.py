def f(n):
    if n == 0: return 5
    if n > 0: return 3 * f(n - 4)
    return f(n + 3)

print(f(43))
