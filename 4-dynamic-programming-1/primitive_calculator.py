# 2021-03-25-09-31-31.png
import math


class calculationType:
    def __init__(self, value, cType):
        self.value = value
        self.cType = cType


def stepsCounter(target, calculationList):
    stepsList = [target]
    dynamicList = [math.inf]*(target+1)

    dynamicList[0] = 0
    dynamicList[1] = 0
    for x in range(2, len(dynamicList)):

        for y in calculationList:

            if y.cType == "addition" and x-(y.value) >= 1 and type(x-(y.value)) == int:

                dynamicList[x] = min(
                    dynamicList[x], dynamicList[x-(y.value)]+1)

            if y.cType == "multiplication" and x/(y.value) >= 1 and x % (y.value) == 0:

                dynamicList[x] = min(
                    dynamicList[x], dynamicList[int(x/(y.value))]+1)

            if y.cType == "substraction" and x+(y.value) >= 1 and type(x+(y.value)) == int:

                dynamicList[x] = min(
                    dynamicList[x], dynamicList[x+(y.value)]+1)

            if y.cType == "division" and x*(y.value) >= 1 and type(x*(y.value)) == int:

                dynamicList[x] = min(
                    dynamicList[x], dynamicList[x*(y.value)]+1)

    print(dynamicList[-1])

    while target > 1:
        templist = []
        # thoda shortcut le rha kyuki aage bhi karna hai re varna calcuation list mein check karta saare elements..
        if target % 3 == 0 and target/3 >= 1:
            templist.append([dynamicList[int(target/3)], 3])
        if target % 2 == 0 and target/2 >= 1:
            templist.append([dynamicList[int(target/2)], 2])
        if target-1 >= 1:
            templist.append([dynamicList[int(target-1)], 1])

        templist.sort()
        if len(templist) >= 1:
            if templist[0][1] == 3:
                target /= 3
            elif templist[0][1] == 2:
                target /= 2
            elif templist[0][1] == 1:
                target -= 1
            stepsList.append(target)
    stepsList.reverse()
    print(stepsList)


if __name__ == '__main__':
    stepsCounter(1, [calculationType(1, "addition"), calculationType(
        2, "multiplication"), calculationType(3, "multiplication"), ])
    stepsCounter(5, [calculationType(1, "addition"), calculationType(
        2, "multiplication"), calculationType(3, "multiplication"), ])
    stepsCounter(96234, [calculationType(1, "addition"), calculationType(
        2, "multiplication"), calculationType(3, "multiplication"), ])
