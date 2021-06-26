from collections import deque
import math


def isBipartite(edgeList):
    visitedList = [False for x in range(len(edgeList))]
    nodeQueue = deque()
    typeList = [math.inf for x in range(len(edgeList))]
    nodeQueue.append(0)
    typeList[0] = 0

    while len(nodeQueue) != 0:
        currentNode = nodeQueue.pop()
        visitedList[currentNode] = True
        for x in edgeList[currentNode]:
            if visitedList[x] == False:
                nodeQueue.append(x)
                visitedList[x] = True
                typeList[x] = 1 if typeList[currentNode] == 0 else 0
            elif visitedList[x] == True and typeList[x] == typeList[currentNode]:
                print(False)
                return

    print(True)


if __name__ == '__main__':
    isBipartite(

        [
            [3],
            [3, 4],
            [3],
            [0, 1, 2],
            [1]
        ]
    )
    # isBipartite(

    #     [
    #         [1, 2, 3],
    #         [0, 2],
    #         [0, 1],
    #         [0]
    #     ]
    # )
