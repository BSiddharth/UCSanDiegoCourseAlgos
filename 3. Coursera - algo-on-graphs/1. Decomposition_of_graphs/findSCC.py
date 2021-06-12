# instead of using kosaraju algo as taught in the course we will be using tarjan's algo for finding SCC.
# https://www.youtube.com/watch?v=TyWtx7q2D7Y this is a great video to learn the algo

def findSCCHelper(x, lowLinkList, visitedList, pathList, graphEdgeList, scclist):
    lowLinkList[x] = x
    # print('setting lowlink value of', x)
    visitedList[x] = True
    pathList.append(x)
    for y in graphEdgeList[x]:
        # print('checking nebur', y, 'of', x)
        if visitedList[y] == True and y in pathList:

            # print(y, 'was visited and in path from', x)
            lowLinkList[x] = min(lowLinkList[x], lowLinkList[y])
            # print('setting the low link of ', x, 'as', lowLinkList[x])

            # print(y, 'was visited but not in path')

        elif visitedList[y] == False:
            # print(y, 'was not visited')
            findSCCHelper(y, lowLinkList, visitedList,
                          pathList, graphEdgeList, scclist)
            if y in pathList:
                # print(y, 'is in path coming back')
                lowLinkList[x] = min(lowLinkList[x], lowLinkList[y])
                # print('setting the low link of ', x, 'as', lowLinkList[x])

    if lowLinkList[x] == x:
        # print("low link matched for", x)
        scc = []
        while len(pathList) != 0 and lowLinkList[pathList[-1]] == x:
            scc.append(pathList.pop())
            # print('scc is', scc)

        scclist.append(scc)
        # print('scclist is', scclist)


def findSCC(graphEdgeList):
    lowLinkList = [x for x in range(len(graphEdgeList))]
    visitedList = [False for x in range(len(graphEdgeList))]
    pathList = []
    scclist = []
    for x in range(len(graphEdgeList)):
        # print("checking node", x)
        if visitedList[x] == False:
            # print(x, 'was not visited so visiting it')
            findSCCHelper(x, lowLinkList, visitedList,
                          pathList, graphEdgeList, scclist)
    print(scclist)


if __name__ == '__main__':
    findSCC([
        [],
        [0],
        [0, 1],
        [0, 2],
        [2, 1],

    ])
