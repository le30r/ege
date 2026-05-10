from turtledemo.penrose import start

f = open("26 (4).txt")
n = int(f.readline())
a = []
for i in range(0, n):
    s = f.readline().split()
    a.append((int(s[0]), int(s[1])))
a.sort()
# номер строки - все её точки
d = dict()
for i in range(0, n):
    j, p = a[i][0], a[i][1]
    if j in d:
        if d[j][-1] != p:
            d[j].append(p)
    else:
        d[j] = [p]
mx = 0
num = 0
for k, dots in d.items():# k  номер строки; v - номера ячейки
    st = dots[0]
    last = dots[0]

    for i in range(1, len(dots)): # по всем точкам в строке
        if dots[i] - last <= 8: # если между светлыми точками 7 тёмных
            last = dots[i] # обновляем номер последней ячейки
        else:
            l = last - st + 1 # считаем длину линии
            if l >= mx: # если длина больше максимальной
                mx = l # обновляем максимум
                num = k # обновляем номер строки

            st = dots[i] # новая линия
            last = dots[i] # новая линия

    l = last - st + 1 # ещё раз проверяем максимум для последней линии
    if l >= mx:
        mx = l
        num = k


print(num, mx)


