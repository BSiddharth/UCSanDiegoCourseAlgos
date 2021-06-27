# 2021-06-26-23-30-08.png
# because we know that all the weights are positives we are gonna use dijkstra algo.
import math
from pqdict import PQDict  # indexed priority queue


def minCost(graph, source, destination):
    distanceList = [math.inf for x in range(len(graph))]
    distanceList[source] = 0
    visitedList = [False for x in range(len(graph))]
    pq = PQDict({})
    pq[str(source)] = 0
    while len(pq) != 0:
        currentNode, currenDistance = pq.popitem()
        currentNode = int(currentNode)
        for x in graph[currentNode]:

            if visitedList[x[0]] == False:
                if distanceList[currentNode] + x[1] < distanceList[x[0]]:
                    distanceList[x[0]] = distanceList[currentNode] + x[1]
                    pq[x[1]] = distanceList[currentNode] + x[1]
        visitedList[currentNode] = True
        if currentNode == destination:
            print(distanceList[currentNode])
            return

    for edge in range(len(graph)):
        pq[str(edge)] = 0


if __name__ == '__main__':
    minCost([[[1, 4], [2, 2]], [[2, 3], [3, 2], [4, 3]], [
            [1, 1], [3, 4], [4, 4]], [], [[3, 1]]], 0, 4)  # 6
    minCost([[[1, 1], [2, 5]], [[2, 2]], [], [[0, 2]]], 0, 2)  # 3
