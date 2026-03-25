f = open("17_23276.txt")
a = []
for i in f:
    a.append(int(i))
f.close()
mx = -1000001 # макс. элемент посл, ок. на 25
for i in a:
    if abs(i) % 100 == 25:
        mx = max(mx, i)
c = 0
s_max = -100000001
for i in range(0, len(a) - 2):
    l = [a[i], a[i + 1], a[i + 2]]
    four_digits = 0
    for j in l:
        if 999 < abs(j) < 10000:
            four_digits += 1
    s = sum(l) # сумма тройки
    if four_digits <= 2 and s <= mx:
        c += 1
        s_max = max(s_max, s)
print(c, s_max)
