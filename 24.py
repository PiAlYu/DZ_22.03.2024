fin = open('24.txt')
s = fin.readline()
fin.close()
print(s)
k, m = 1, 1
for i in range(1, len(s) - 1):
    if (s[i] == s[i + 1] or s[i] == s[i - 1]) and s[i] in 'AC':
        k += 1
    else:
        m = max(m, k)
        k = 0
print(m // 2)
