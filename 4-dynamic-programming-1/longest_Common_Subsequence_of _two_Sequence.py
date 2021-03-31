# 2021-03-30-17-33-16.png
import math


def findIt(list1, list2):
    dynamiclist = [[-math.inf for y in range(
        len(list2)+1)] for x in range(len(list1)+1)]

    for x in range(len(list1)+1):
        for y in range(len(list2)+1):
            if x == 0 or y == 0:
                dynamiclist[x][y] = 0

    for x in range(1, len(list1)+1):
        for y in range(1, len(list2)+1):
            if list1[x-1] == list2[y-1]:
                dynamiclist[x][y] = 1 + dynamiclist[x-1][y-1]
            else:
                dynamiclist[x][y] = max(
                    dynamiclist[x][y-1],
                    # dynamiclist[x-1][y-1],
                    dynamiclist[x-1][y])

    print(dynamiclist[-1][-1])


if __name__ == '__main__':
    findIt([2, 7, 5], [2, 5]),  # 2
    findIt([7], [1, 2, 3, 4]),  # 0
    findIt([2, 7, 8, 3], [5, 2, 8, 7]),  # 2
    findIt(['A', 'B', 'C', 'D', 'G', 'H'], [
           'A', 'E', 'D', 'F', 'H', 'R']),  # 3
    findIt(['A', 'G', 'G', 'T', 'A', 'B'], ['G', 'T', 'A', 'B']),  # 4
