# find in union-find of disjoint set
def find(parentList, i):
    if parentList[i] == i:
        return i
    else:
        return find(parentList, parentList[i])


# union in union-find of disjoint set
def union(rankList, parentList, x, y):
    xRoot = find(parentList, x)
    yRoot = find(parentList, y)

    if rankList[x] < rankList[y]:
        parentList[xRoot] = yRoot
    elif rankList[x] > rankList[y]:
        parentList[yRoot] = xRoot
    else:
        parentList[yRoot] = xRoot
        rankList[y] += 1


def kruskals(totalVertices, graph):
    # sorting graph according to the weight. deleting is expensive compared to heap so we will not pop just iterate.
    graph.sort(key=lambda x: x[2])

    # this is the parent list for find in union-find of disjoint set
    parentList = [x for x in range(totalVertices)]
    rankList = [0 for x in range(totalVertices)]

    mst = []

    # numOfEdgesFormed = 0
    # while numOfEdgesFormed < totalVertices - 1:
    for x, y, weight in graph:
        if find(parentList, x) != find(parentList, y):
            union(rankList, parentList, x, y)
            # numOfEdgesFormed += 1
            mst.append([x, y, weight])
    totalWeight = 0
    for x, y, weight in mst:
        totalWeight += weight
    print('Minimum spanning tree is', mst, 'and total weight is', totalWeight)


if __name__ == '__main__':
    kruskals(9, [[0, 1, 28], [0, 5, 10], [1, 6, 14], [1, 2, 16], [
             2, 3, 12], [3, 4, 22], [3, 6, 18], [6, 4, 24], [4, 5, 25]])
