# 2021-04-02-12-35-53.png

def maxWeight(W, w):
    dynamiclist = [[0 for x in range(len(w)+1)] for x in range(W+1)]
    for x in range(1, W+1):
        for y in range(1, len(w)+1):
            if w[y-1] <= x:
                dynamiclist[x][y] = max(
                    dynamiclist[x][y], dynamiclist[x][y-1], dynamiclist[x-w[y-1]][y-1]+w[y-1])
            else:
                dynamiclist[x][y] = dynamiclist[x][y-1]

    print(dynamiclist[-1][-1])


if __name__ == '__main__':
    maxWeight(10, [1, 4, 8]),
    maxWeight(16, [6, 8, 10]),
    maxWeight(10, [1, 1, 1, 6, 2, 2]),
    maxWeight(34, [9, 8, 5, 28, 14, 12]),
