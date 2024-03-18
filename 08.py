c = set()
for b in range(5 ** 4, 5 ** 5 - 1):
    for a in range(b + 1, 5 ** 5):
        c.add(a - b)
print(len(c))
