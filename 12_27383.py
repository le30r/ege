# ПОКА нашлось (12)
# заменить (12, 4)

for n in range(0, 20):
    s = ""
    for i in range(0, n):
        s += '12'
    s += "1" * (10 - n)


    while '12' in s:
        s = s.replace('12', '4', 1)
    r = s.count('1') + s.count('2') * 2 + s.count('4') * 4
    if r == 25:
     print(n)

# 111111114222
# 1212121212
# 12 -> 4
# 12 12 12 111 111 1
