# 2021-03-13-23-34-07.png

def findMajority(listy):
    listy.sort()
    currentNumber = listy[0]
    count = 0

    for n in range(len(listy)):
        if listy[n] == currentNumber:
            count += 1
            if count > len(listy)//2:
                print(1)
                return
        else:
            currentNumber = listy[n]

    print(0)

# This algo can do this in O(nlogn) but Moore’s Voting Algorithm can do this in O(n)


def mooreMajority(listy):
    count = 0
    currentNum = listy[0]
    for n in listy:
        if n == currentNum:
            count += 1
        else:
            count -= 1
            if count == 0:
                currentNum = n
                count = 1
    count = 0
    for n in listy:
        if n == currentNum:
            count += 1
    if count > len(listy)//2:
        print(1)

    else:
        print(0)


if __name__ == '__main__':
    findMajority([2, 3, 9, 2, 2])
    findMajority([1, 2, 3, 4])
    findMajority([1, 2, 3, 1])

    mooreMajority([2, 3, 9, 2, 2])
    mooreMajority([1, 2, 3, 4])
    mooreMajority([1, 2, 3, 1])
