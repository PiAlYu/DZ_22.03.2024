fin = open('27-B.txt')
a = [int(i) for i in fin.readlines()]
fin.close()
a.pop(0)
k, d = 0, 0
pr = [0 for i in range(len(a))]
m = [[0 for i in range(a.count(0) + 1)] for j in range(2)]
for i in range(len(a)):
    if a[i] == 0:
        d += 1
    pr[i] = d
m = [[0 for i in range(a.count(0) + 1)] for j in range(2)]
for i in range(len(a)):
    if a[i] != 0:
        for j in range(a.count(0)):
            if j != pr[i]:
                k += m[a[i] % 2][j]
        m[a[i] % 2][pr[i]] += 1
print(k)
