from math import dist


def find_center(points):
    min_sum = 100000000000
    best = None

    for cand in points:
        s = sum(abs(dist(cand, p)) for p in points)
        if s < min_sum:
            min_sum = s
            best = cand

    return best

f = open("27_А.txt")
data = [] # необработанный массив данных


for s in f:
    x,y = s.split()
    data.append([float(x), float(y)])


cluster1 = []
cluster2 = []
cluster3 = []
# пока не обработали все точки
for p in data:
    if p[1] < -5:
        cluster1.append(p)
    if 11 < p[0] < 35 and -5 < p[1] < 11:
        cluster2.append(p)
    else:
        cluster3.append(p)


print(len(cluster1), len(cluster2), len(cluster3))

Px = 0
Py = 0
c1 = find_center(cluster1)
Px += c1[0]
Py += c1[1]

c2 = find_center(cluster2)
Px += c2[0]
Py += c2[1]


c3 = find_center(cluster3)
Px += c3[0]
Py += c3[1]


print(abs((Px / 3)) * 100000, abs((Py / 3)) * 100000)
