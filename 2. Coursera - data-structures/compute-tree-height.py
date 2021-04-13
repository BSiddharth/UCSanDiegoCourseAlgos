# 2021-04-08-10-37-25.png
# from basicDS import TreeNode, Tree


# def buildTree(parentNodeList):
#     treeNodeList = []
#     for x in range(len(parentNodeList)):
#         node = TreeNode()
#         treeNodeList.append(node)

#     for x in range(len(parentNodeList)):
#         if parentNodeList[x] == -1:
#             tree = Tree(treeNodeList[x])
#         else:
#             treeNodeList[parentNodeList[x]].children.append(treeNodeList[x])

#     return tree

def findHeightHelper(x, parentNodeList, visited, height):
    if visited[x] == 1:
        return height[x]
    elif parentNodeList[x] == -1:
        visited[x] = 1
        height[x] = 1
        return height[x]
    else:
        return 1 + findHeightHelper(parentNodeList[x], parentNodeList, visited, height)


def findHeight(parentNodeList):
    # tree = buildTree(parentNodeList)
    # print(findHeightHelper(tree))

    n = len(parentNodeList)
    visited = [0]*n
    height = [0]*n
    maxHeight = 0

    for x in range(len(parentNodeList)):
        maxHeight = max(maxHeight, findHeightHelper(
            x, parentNodeList, visited, height))

    print(maxHeight)
# def findHeightHelper(tree):
#     if tree.length == 0:
#         return 0


if __name__ == '__main__':
    findHeight([4, -1, 4, 1, 1]),
    findHeight([-1, 0, 4, 0, 3]),
