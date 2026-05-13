from math import *

f = open('27_A_83157.txt')
points = [list(map(float, s.split())) for s in f]
k = 2
clusters = [[] for i in range(k)]
for x, y in points:
    if y < 90:
        clusters[0].append([x, y])
    else:
        clusters[1].append([x, y])
print(len(clusters))
best_center = [[] for i in range(k)]
print(len(clusters[0]))
print(len(clusters[1]))

for i in range(k):
    max_sum_dist = 0
    for x1, y1 in clusters[i]:
        sum_dist = 0
        for x2, y2 in clusters[i]:
            sum_dist += dist([x1, y1], [x2, y2])
        if max_sum_dist <= sum_dist:
            max_sum_dist = sum_dist
            best_center[i] = [x1, y1]
P_1 = abs((best_center[1][0] + best_center[1][1]) * 10_000)
P_2 = abs((best_center[0][0] + best_center[0][1]) * 10_000)
print(int(P_1), int(P_2))