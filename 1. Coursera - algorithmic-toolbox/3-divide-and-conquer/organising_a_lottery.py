# 2021-03-20-14-14-32.png

def naiveTellNa(seg, pts):
    tempList = [0]*len(pts)
    for x in range(len(pts)):
        count = 0
        for y in seg:
            if y[0] <= pts[x] and y[1] >= pts[x]:
                count += 1
        tempList[x] = count
    print(tempList)


# optimized way samaj nhi aarha https://www.geeksforgeeks.org/find-number-of-segments-covering-each-point-in-an-given-array/ isme se padloonga baadme
#  this was helpful https://stackoverflow.com/questions/33752703/points-and-segments/33752996

def myFunc(element):
    return element[0]


def optimizedTellNa(seg, pts):
    tempList = [0]*len(pts)
    sortedList = []
    counter = 0
    for x in seg:
        sortedList.append([x[0], +1, "open"])
        sortedList.append([x[1], -1, "zclose"])
        # z isiliye daala hai jisse point phele sort ho

    for x in range(len(pts)):
        sortedList.append([pts[x], x, "point"])
        # ye point phele sort ho isiliye z daala close mei

    sortedList.sort(key=myFunc)

    for x in range(len(sortedList)):
        if sortedList[x][2] == "open":
            counter += 1
        elif sortedList[x][2] == "zclose":
            counter -= 1
        else:
            tempList[sortedList[x][1]] = counter

    print(tempList)


if __name__ == '__main__':
    naiveTellNa([(1, 6), (8, 10), (5, 9)], [5, 8, 2])
    optimizedTellNa([(1, 6), (8, 10), (5, 9)], [5, 8, 2])
    naiveTellNa([(0, 5), (7, 10)], [1, 6, 11])
    optimizedTellNa([(0, 5), (7, 10)], [1, 6, 11])
    naiveTellNa([(-10, 10)], [-100, 100, 0])
    optimizedTellNa([(-10, 10)], [-100, 100, 0])
    naiveTellNa([(0, 5), (-3, 2), (7, 10)], [1, 6])
    optimizedTellNa([(0, 5), (-3, 2), (7, 10)], [1, 6])
