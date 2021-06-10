from collections import deque


# class GraphNode:
#     def __init__(self, value) -> None:
#         self.checked = False
#         # self.type = "entry"
#         self.value = value
#         self.neighbours = []

# def printTopoHelper(graphNodeneburs,checklist):


# def printTopo(graph):
#     # stack = deque()
#     # stack.append(0)
#     # while len(stack) != 0:
#     #     for x in graphEdgeList[]
#     checklist = [False for x in len(graphEdgeList)]
#     printTopoHelper(graphEdgeList[0],checklist)

def printTopoHelper(x, visitedlist, edgeList, stack):
    if visitedlist[x] == False:
        visitedlist[x] = True
        for y in edgeList[x]:
            printTopoHelper(y, visitedlist, edgeList, stack)
        stack.append(x)


def printTopo(edgeList):
    visitedlist = [False for x in range(len(edgeList))]
    stack = deque()
    for x in range(len(edgeList)):
        printTopoHelper(x, visitedlist, edgeList, stack)

    while len(stack) != 0:
        print(stack.pop(), end=" ")


if __name__ == '__main__':
    printTopo([[], [0], [0, 1], [0, 2], [2, 1]])
