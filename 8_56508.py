# Определите количество чисел, для записи которых в восьмеричной системе счисления требуется ровно 11 цифр,
# ровно 3 из которых— нечётные, и никакие две нечётные цифры не стоят рядом.
# ['1', '3', '5', '7'] -> "1257"
# ['1', '3', '5', '7'] "."-> "1.2.5.7"
import itertools
from itertools import repeat

# import itertools
#
# a = ['Ч', 'Н', 'Ч', 'Н', 'Ч', 'Н', 'Ч', 'Н']
# nech = ['1', '3', '5', '7']
# ch = ['0', '2', '4', '6']
# k = 0
# p = itertools.product(a, repeat = 11)
# for i in p:
#     s = "".join(i)
#     if s.count("Н") == 3 and s.count("НН") == 0:
#         k += 1
# print(k)


p = itertools.product("НЧ", repeat=11)
st = set()
ch = 0
nch = 0
for i in p:
    s = "".join(i)
    if s.count("Н") == 3 and s.count("НН") == 0:
        print(s)
        if s[0] == "Н":
            nch += 1
        else:
            ch += 1
l = len(st)
print(4 ** 11 * nch + 3 * 4 ** 10 * ch)

# НЧ НЧ НЧ  Ч Ч Ч Ч Ч
# ЧН ЧН ЧН  Ч Ч Ч Ч Ч
