fin = open('18.csv')
s = fin.readlines()
fin.close()
s = [int(i) for i in s]
print(s)
k, m = 1, 0
for i in range(1, len(s)):
    if s[i] % 10 == s[i - 1] % 10:
        k += 1
    else:
        m = max(m, k)
        k = 1
print(m)
