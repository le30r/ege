from math import dist


def cluster_diam(cluster1, cluster2):
    res = []

    for p1 in cluster1:
        for p2 in cluster2:
            res.append([dist(p1, p2), p1, p2])

    return max(res)

f = open("27_А.txt")
data = [] # необработанный массив данных


for s in f:
    x,y = s.split()
    data.append([float(x), float(y)])

clusters = []
rast = 4.95

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
    #if len(cl) > 1:
    clusters.append(cl)

clusters.sort(key=len)
print([len(cl) for cl in clusters])
diams = []

for i in range(len(clusters)):
    for j in range(i + 1, len(clusters)):
        clusters_diam = cluster_diam(clusters[i], clusters[j])
        diams.append(clusters_diam)

Q1 = 0
Q2 = 0
for d in diams:
    Q1 += d[0]
    p1 = d[1]
    p2 = d[2]
    p1_dist = dist([2, 2], p1)
    Q2 = max(p1_dist, Q2)

    p2_dist = dist([2, 2], p2)
    Q2 = max(p2_dist, Q2)

print(int(Q1 * 100), int(Q2 * 100))



