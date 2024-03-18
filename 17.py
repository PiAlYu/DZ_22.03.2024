fin = open('17.txt')
s = fin.readlines()
fin.close()
s = [int(i) for i in s]
print(s)
a = sum(s) / len(s)
b, k = 0, 0
for i in range(1, len(s) - 2):
    if s[i] * s[i + 1] > s[i - 1] * s[i + 2]:
        b = max(b, s[i] + s[i + 1])
        if s[i] > a or s[i + 1] > a:
            k += 1
print(b, k)
