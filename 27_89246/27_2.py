from fnmatch import fnmatch
from math import dist

def find_center(points):
    min_sum = 100000000000
    best = None

    for cand in points:
        s = sum(dist(cand[0], p[0]) for p in points)
        if s < min_sum:
            min_sum = s
            best = cand

    return best

f = open("27_B (2).txt")
data = [] # необработанный массив данных


for s in f:
    x,y,ch = s.split()
    coords = (float(x), float(y))
    data.append((coords, ch))

clusters = []
rast = 2

# пока не обработали все точки
while data:
    cl = [data.pop()]

    for p in cl:
        neigh = []
        for p1 in data:
            if dist(p[0], p1[0]) < rast:
                neigh.append(p1)

        for p1 in neigh:
            cl.append(p1)
            data.remove(p1)

    clusters.append(cl)

i = 0
for cl in clusters:
    c = 0
    for st in cl:
        if fnmatch(st[1], "A?I"):
            c += 1
    print(i, c)
    i += 1

center_0 = find_center(clusters[0])
center_2 = find_center(clusters[2])
print(dist(center_0[0], center_2[0]) * 10000)

max_dist = 0
for i in range(0, len(clusters)):
    for p in clusters[i]:
        for p1 in clusters[i]:
            if fnmatch(p[1], "A?V") and fnmatch(p1[1], "A?V"):
                max_dist = max(max_dist, dist(p[0], p1[0]))
print(max_dist * 10000)