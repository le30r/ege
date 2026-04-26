from math import dist


f = open("27_A (1).txt")
data = [] # необработанный массив данных


for s in f:
    x,y = s.split()
    data.append([float(x), float(y)])

clusters = []
rast = 2

# пока не обработали все точки
while data:
    cl = [data.pop()]

    for p in cl:
        neigh = []
        for p1 in data:
            if dist(p, p1) < rast:
                neigh.append(p1)

        for p1 in neigh:
            cl.append(p1)
            data.remove(p1)

    clusters.append(cl)


cluster1 = clusters[0]
cluster2 = clusters[1]

res = []

for p1 in cluster1:
    for p2 in cluster2:
        res.append([dist(p1, p2), p1, p2])

m = max(res)

Px = abs(m[1][0] + m[2][0]) * 1000
Py = abs(m[1][1] - m[2][1]) * 1000

print(int(Px), int(Py))
