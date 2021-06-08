# 2021-06-03-22-58-45.png

from collections import deque


class GraphNode:
    def __init__(self, value) -> None:
        self.checked = False
        self.type = "entry"
        self.value = value
        self.neighbours = []

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        # return " ".join(str(self.neighbours.value))
        # return " ".join(list(map(lambda x: str(x.value), self.neighbours)))
        # return str(self.neighbours)
        return str(self.value)


def checkForCycles():
    totalNodes, totalEdges = list(map(lambda x: int(x), input().split()))

    nodelist = [GraphNode(x+1) for x in range(totalNodes)]
    pathlist = [False for x in range(totalNodes)]
    for x in range(totalEdges):

        x, y = list(map(lambda x: int(x), input().split()))

        nodelist[x-1].neighbours.append(nodelist[y-1])
        # print('neburs of', nodelist[x-1].value,
        #       'are', nodelist[x-1].neighbours)

    # print("the node list is:", nodelist)

    nodeStack = []
    nodeStack.append(nodelist[0])
    # print("node stack is:", nodeStack)
    while len(nodeStack) != 0:
        if nodeStack[-1].type == "entry":

            currentNode = nodeStack[-1]
            # print("current node:", currentNode)
            currentNode.checked = True
            pathlist[currentNode.value - 1] = True
            # print('path list is:', pathlist)
            currentNode.type = "exit"
            # print('current nodes nebur are', currentNode.neighbours)
            for x in currentNode.neighbours:
                if x.checked == False:
                    nodeStack.append(x)
                    # print('node to be added is', x)
                    # print("after appending the node stack is:", nodeStack)
                elif pathlist[x.value - 1] == True:
                    print(1)
                    return
        else:

            pathlist[nodeStack[-1].value-1] = False
            # print('path list after removing is:', pathlist)
            nodeStack.pop()

    print(0)
    return


if __name__ == '__main__':
    checkForCycles(),
