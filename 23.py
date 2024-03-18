def f(a, h):
    if h == 5: return a
    return f'{f(a + 4, h + 1)} {f(a * 2, h + 1)}'

print(len(set(f(2, 0).split())))
