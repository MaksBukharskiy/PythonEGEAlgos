from math import *

clustersA = [[], []]
clustersB = [[], [], []]

for s in open("2A.txt"):
    s = s.replace(",", ".")
    x, y = map(float, s.split())

    if y>10: clustersA[0].append([x, y])
    else: clustersA[1].append([x, y])

for s in open("2B.txt"):
    s = s.replace(",", ".")
    x, y = map(float, s.split())

    if 0<x<20:
        if y < 10: clustersB[0].append([x, y])
        elif y > 21: clustersB[1].append([x, y])
        else: clustersB[2].append([x, y])


def findCenter(cluster):
    minsum = 10**10
    best = []

    for p in cluster:
        summ = sum(dist(p, p1) for p1 in cluster)
        if summ<minsum:
            minsum = summ
            best = p

    return best

centersA = [findCenter(cl) for cl in clustersA]

px = abs(int(max(p[0] for p in centersA) * 10000))
py = abs(int(max(p[1] for p in centersA) * 10000))

print(px)
print(py)

