# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов X.
# Хотя бы один символ X находится в последовательности.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open("24_demo (1).txt")
s = f.readline()
n = len(s)
c = 0
mx = 0
for i in range(n):
    if s[i] == 'X':
       c += 1
    else:
        c = 0
    mx = max(c, mx)
print(mx)

# XXXYYXXYZXXYXZYXXXYYXXXXXXXXYZXYXXXYXYZYYZXYXXXXXXXXXYXZXYYXYYYXXXYXYZYYXYXYZXYXXYYXZXXXXYXZXYXYXXXYXXZXXYYZYXXXYYYYZXYYXXZXXXXYXXXYXXXZZXXXZYYZXXZXXXYXXYXXYYXYYXZYXYXZXZYXXYXXXYXXXZYYYYXXXXXZXZXXYXZXZXXZZZYYZXXXXYYZXZYXYYXXZYYXXYXZXXZXXYYXXZXXYYXZXXYXZYXXXXYZXZYXXXYXYYXYXYZYXXXXYXYXXXYXXXXXYYXYXYYXXYZXZYXYXYYZXXXZYXYYYYZYYYZYXXXYYYYYYXZXYYZXZYYXYZZXZXXZYYYYXXXYYXXXXYXZXXYXYXXYYZZZXXYXXXYXYXYXXYZXXYZXXXYXYYXZ
# |
