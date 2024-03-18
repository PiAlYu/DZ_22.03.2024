def f(n):
    s = []
    for i in range(int(n ** 0.5) + 1, 0, -1):
        if n % i == 0:
            if str(i)[0] == '4':
                s.append(i)
            if str(n // i)[0] == '4':
                s.append(n // i)
    if len(s) != 0:
        return len(s) == 24, max(s)
    return False, 0

for i in range(1, 10 ** 6):
    a = f(i)
    if a[0]:
        print(i, a[1])
