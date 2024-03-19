from itertools import product

k = 0
for i in product('01', repeat = 7):
    a = [int(j) for j in i]
    f = a[3] or (a[0] * a[1] * a[4] * a[5] * a[6] * (not(a[2])))
    if f == 0:
        k += 1
print(k)
