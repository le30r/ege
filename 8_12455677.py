#Сколько существует десятичных четырёхзначных чисел,
# в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?

def mod2(a):
    return int(a) % 2 == 0

a = '0123456789'
k = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                s = a1 + a2 + a3 + a4
                r = {a1, a2, a3, a4}
                if len(r) == 4 and mod2(a1) != mod2(a2) and mod2(a2) != mod2(a3) and mod2(a3) != mod2(a4) and a1 != '0':
                    k += 1
print(k)