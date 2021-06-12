from collections import deque
import math


def minSeg(edgeList, start, destination):
    visitedList = [False for x in range(len(edgeList))]
    nodeQueue = deque()
    nodeQueue.append(start)
    distanceList = [math.inf for x in range(len(edgeList))]
    distanceList[start] = 0

    while len(nodeQueue) != 0:
        currentNode = nodeQueue.pop()
        visitedList[currentNode] = True
        for x in edgeList[currentNode]:
            if visitedList[x] == False:
                nodeQueue.append(x)
                visitedList[x] = True
                distanceList[x] = distanceList[currentNode] + 1
                if x == destination:
                    print(distanceList[x])
                    return
    print(-1)


if __name__ == '__main__':
    minSeg([
        [2, 3],
        [4],
        [0, 3],
        [0, 2],
        [1],
    ], 2, 4)
    # minSeg([
    #     [1, 2, 3],
    #     [0, 2],
    #     [0, 1],
    #     [0]
    # ], 1, 3)
