# 2021-04-02-12-35-53.png

def maxWeight(W, w):
    dynamiclist = [[0 for x in range(len(w)+1)] for x in range(W+1)]
    for x in range(w+1):
        for y in range(len(w)+1):
            if x == 0 or y == 0:
                dynamiclist[x][y] = 0
    for x in range(1, w+1):
        for y in range(1, len(w)+1):
            # dynamiclist[x][y] = max(dynamiclist[x][y], dynamiclist[x-1][y], dynamiclist[][])
            pass


if __name__ == '__main__':
    maxWeight(10, [1, 4, 8]),
    maxWeight(16, [6, 8, 10]),
    maxWeight(10, [1, 1, 1, 6, 2, 2]),
