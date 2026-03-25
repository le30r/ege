# Определите количество шестеричных пятизначных чисел,
# в записи которых не менее двух цифр 5 и не более трёх нечетных цифр, меньших 4.

a = '012345'
k = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    s = a1 + a2 + a3 + a4 + a5
                    u = []
                    for i in s:
                        if int(i) % 2 == 1 and int(i) < 4:
                            u.append(i)

                    if a1 != '0' and s.count("5") >= 2 and len(u) <= 3:
                        k += 1
print(k)