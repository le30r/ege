#Текстовый файл состоит из символов A, C, D, F и O.
#Определите максимальное количество идущих подряд пар символов вида:
#согласная + гласная.

f = open("24 (2).txt")
s = f.readline()
l = 0
m = 0
sogl = ['C', 'D', 'F']
gl = ['A', 'O']
i = 0
while i < len(s) - 1:
    if s[i] in sogl and s[i + 1] in gl:
        l += 1
        i += 2
    else:
        m = max(m, l)
        l = 0
        i += 1
print(m)

# OFAFOFOCADOCAFOCODOCOCADOCOFCFADOCACOCAFODAFDC
