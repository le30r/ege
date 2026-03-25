f = open("1777.txt")
a = [] # исходный список
for i in f:
    a.append(int(i))
f.close()
c = 0 # количество троек удовл. условию
m = -1_000_001 # макс элемент. оканч. на 29
for i in range(len(a)): # цикл с поиском макс. элемента ок. на 29
    if abs(a[i]) % 100 == 29:
        m = max(m, a[i])
s_max = -3_000_001 # максимальная сумма троек
for i in range(len(a) - 2): # основной цикл
    s = [a[i], a[i+1],  a[i+2]] # тройка
    five_digits = 0 # количество пятизначных элементов
    for x in s: # x - элемент тройки
        if 9999 < abs(x) < 100000:
            five_digits += 1
    if five_digits == 2 and sum(s) <= m:
        s_max = max(s_max, (a[i] + a[i+1] + a[i+2]))
        c += 1
print(c, s_max)