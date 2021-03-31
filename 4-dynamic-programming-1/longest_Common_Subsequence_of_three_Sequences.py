# 2021-03-31-17-32-43.png
import math


def findIt(list1, list2, list3):

    dynamiclist = [[[-math.inf for z in range(len(list3)+1)]
                    for y in range(len(list2)+1)] for x in range(len(list1)+1)]

    for x in range(len(list1)+1):
        for y in range(len(list2)+1):
            for z in range(len(list3)+1):
                if x == 0 or y == 0 or z == 0:
                    dynamiclist[x][y][z] = 0

    for x in range(1, len(list1)+1):
        for y in range(1, len(list2)+1):
            for z in range(1, len(list3)+1):
                if list1[x-1] == list2[y-1] == list3[z-1]:
                    dynamiclist[x][y][z] = 1 + dynamiclist[x-1][y-1][z-1]
                else:
                    dynamiclist[x][y][z] = max(
                        dynamiclist[x-1][y-1][z-1], dynamiclist[x -
                                                                1][y][z], dynamiclist[x][y-1][z], dynamiclist[x][y][z-1],
                        dynamiclist[x-1][y][z-1], dynamiclist[x][y-1][z-1], dynamiclist[x-1][y-1][z])

    print(dynamiclist[-1][-1][-1])


if __name__ == '__main__':
    findIt([1, 2, 3], [2, 1, 3], [1, 3, 5])  # 2
    findIt([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7])  # 3
    findIt([1, 8, 3, 7, 9, 2, 4, 6], [4, 8, 3, 1, 8, 2, 4, 8,
                                      9, 8, 4, 3], [8, 9, 1, 3, 7, 6, 4, 3, 8, 5, 9])  # ?
