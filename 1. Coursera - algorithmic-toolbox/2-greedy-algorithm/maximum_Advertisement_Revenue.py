# 2021-03-02-22-20-50.png

# ppc is profit per click

def getMaxPay(ppcList, clickList):
    ppcList.sort(reverse=True)
    clickList.sort(reverse=True)

    sum = 0
    for x in range(len(ppcList)):
        sum += ppcList[x]*clickList[x]

    print(sum)


if __name__ == '__main__':
    getMaxPay([1, 3, -5], [-2, 4, 1])
