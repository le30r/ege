# В системе счисления с основанием p выполняется равенство zx+xy=zyA.
#
# Буквами x, y, и z обозначены некоторые цифры из алфавита системы счисления с основанием p. Определите значение числа xyz p и запишите это значение в десятичной системе счисления.

a = sorted("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for p in range(11, 37):
    for x in range(1, p):
        for y in range(0, p):
            for z in range(1, p):
                A = a[z] + a[x]
                B = a[x] + a[y]
                C = a[z] + a[y] + "A"
                if (int(A, p) + int(B, p)) == int(C, p):
                    XYZ = a[x] + a[y] + a[z]
                    print(int(XYZ, p))
