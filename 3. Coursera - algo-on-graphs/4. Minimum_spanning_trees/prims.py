import math
from operator import le
from pqdict import pqdict
# pq = pqdict({'a': (0, 4), 'b': (8, 5), 'c': (10, 1)}, key=lambda x: x[1])
# print(pq.popitem())


def prims(graph):
    mst = []
    totalCost = 0
    tempdict = {}
    parentList = [x for x in range(len(graph))]
    for x in range(len(graph)):
        tempdict[x] = math.inf
    tempdict[0] = 0
    pq = pqdict(tempdict)
    print(pq)
    while len(pq) != 0:
        currentNode, currentcost = pq.popitem()

        for toNode, cost in graph[currentNode]:
            if toNode in pq and cost < pq[toNode]:
                pq[toNode] = cost
                parentList[toNode] = currentNode

        totalCost += currentcost
    for x in range(len(parentList)):
        if x != parentList[x]:
            mst.append([x, parentList[x]])
    print(mst, totalCost)


if __name__ == '__main__':
    prims([[[1, 4], [7, 8]], [[2, 8], [7, 11], [0, 4]], [[3, 7], [5, 4], [8, 2], [1, 8]], [[4, 9], [5, 14], [2, 7]], [[5, 10], [3, 9]], [
          [3, 14], [4, 10], [2, 4], [6, 2]], [[5, 2], [8, 6], [7, 1]], [[6, 1], [8, 7], [0, 8], [1, 11]], [[2, 2], [6, 6], [7, 7]]])
