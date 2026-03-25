# Текстовый файл состоит не более чем из 10^6 символов латинского алфавита.
# Определите длину минимальной подстроки, содержащую не менее 130 символов W.
# Для выполнения этого задания следует написать программу.

# WUUYKJKFUWIIUUWWIIRWIWIIWEIIIWIIIJIIWO
# 0,9,14,15,19,21,24

f = open("24 (3).txt")
s = f.readline()
ws = []
for i in range(len(s)):
    if s[i] == 'W':
        ws.append(i)
print(len(ws))
i = 0
j = 129
m = 10 ** 7
while j < len(ws):
    m = min(ws[j] - ws[i] + 1, m)
    i += 1
    j += 1
print(m)
