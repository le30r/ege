f = open("26_demo.txt")
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])

for i in range(0, len(data)):
    data[i] = int(data[i])

data = sorted(data)

summ = 0
for count in range(0, len(data)):
    if summ + data[count] > s:
        break
    summ += data[count]
print(count)
zapas = s - summ
for i in range(count, len(data)):
    if data[i] - data[count - 1] <= zapas:
        last = data[i]
print(last)
