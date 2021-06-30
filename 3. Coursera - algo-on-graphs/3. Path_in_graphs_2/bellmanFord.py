# 2021-06-30-22-18-42.png
# to find if a graph has negative cycle using bellman ford algo
import math
# using 1-indexed graph


def hasNCycle(graph, source):
    graph_len = len(graph)
    distList = [math.inf for x in range(graph_len)]
    distList[source-1] = 0
    didRelax = False
    for loop in range(graph_len-1):
        for edge in graph:
            if distList[edge[1]-1] > distList[edge[0]-1] + edge[2]:
                distList[edge[1]-1] = distList[edge[0]-1] + edge[2]
                didRelax = True
        if not didRelax:
            break
        else:
            didRelax = False
    for edge in graph:
        if distList[edge[1]-1] > distList[edge[0]-1] + edge[2]:
            distList[edge[1]-1] = distList[edge[0]-1] + edge[2]
            didRelax = True
    if didRelax:
        print("Negative cycle exists")
    else:
        print('No negative cycle exists')


if __name__ == '__main__':
    hasNCycle([
        [1, 2, 4], [1, 3, 2], [2, 3, 3], [2, 4, 2],
        [2, 5, 3], [3, 2, 1], [3, 4, 4], [3, 5, 4],
        [5, 4, 1],
    ], 4)
