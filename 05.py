def f(a, b, h):
    if a == b: return h
    elif a > b: return None
    return f(a + 8, b, h + '1') or f(a * 2, b, h + '2')

print(f(45, 376, ''))
