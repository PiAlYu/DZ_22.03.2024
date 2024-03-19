fin = open('26.txt')
a = [int(i) for i in fin.readlines()]
fin.close()
a.pop(0)
a.sort()
k, i, j = 0, 0, 0
while i < len(a):
    j = len(a) - 1
    while j > i:
        if a[i] + a[j] == 100:
            k += 1
            a.pop(i)
            a.pop(j - 1)
            i -= 1
            break
        j -= 1
    i += 1
print(k)
