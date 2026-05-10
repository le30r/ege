f = open("107_27_A.txt")
n = int(f.readline())
print(n)
d = []
for i in f:
    d.append(int(i))

min_S = 10000000000
for i in range(0, n):
    S = 0
    for j in range(0, n - i):
        if j <= n // 2:
            S += d[j + i] * j * 3
        else:
            S += d[i + j] * (n - j) * 3

    for j in range(n - i, n):
        coord = abs(n - j - i)
        if j <= n // 2:
            S += d[coord] * j * 3
        else:
            S += d[coord] * (n - j) * 3

    min_S = min(S, min_S)

print(min_S)
