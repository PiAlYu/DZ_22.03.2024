def f(a):
    p = range(5, 55)
    q = range(50, 94)
    k = 0
    for x in range(1, 1000):
        f = (x not in p and x in q) <= (x > a)
        if f == 0:
            k += 1
    return k == 20

for i in range(1, 1000):
    if f(i) == True:
        print(i)
        break
