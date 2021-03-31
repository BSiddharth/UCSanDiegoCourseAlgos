# 2021-03-29-21-11-44.png

import math


def findEditDistance(str1, str2):
    x = len(str1)
    y = len(str2)
    dynamicList = []
    for i in range(x+1):
        dynamicList.append([math.inf for j in range(y+1)])
    for i in range(x+1):
        for j in range(y+1):
            if i == 0:
                dynamicList[i][j] = j
            elif j == 0:
                dynamicList[i][j] = i
    for a in range(1, x+1):
        for b in range(1, y+1):
            change = dynamicList[a-1][b-1]+1
            insertion = dynamicList[a-1][b]+1
            deletion = dynamicList[a][b-1]+1
            match = dynamicList[a-1][b-1]
            if str1[a-1] == str2[b-1]:
                dynamicList[a][b] = min(change, insertion, deletion, match)
            else:
                dynamicList[a][b] = min(change, insertion, deletion)

    print(dynamicList[x][y])


if __name__ == '__main__':
    findEditDistance('ab', 'ab')  # 0
    findEditDistance('short', 'ports')  # 3
    findEditDistance('editing', 'distance')  # 5
