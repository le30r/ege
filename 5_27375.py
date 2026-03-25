def toN(x, n):
    s = ""
    while x > 0:
        s += str(x % n)
        x //= n
    return s[::-1]

for N in range(1, 100):
    s = toN(N, 3)
    s += str(N % 3)
    print(int(s, 3))