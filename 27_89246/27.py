import fnmatch
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

f = open("27_A (2).txt")
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


max_cluster = clusters[0]
print(len(max_cluster))

center = find_center(max_cluster)
print(center)

min_dist = 100000000000
cand = None
# G..III
for p in max_cluster:
    if fnmatch.fnmatch(p[1], "G?III"):
        if dist(center[0], p[0]) < min_dist:
            min_dist = dist(center[0], p[0])
            cand = p

print(cand[0][0] * 1000, cand[0][1] * 1000)