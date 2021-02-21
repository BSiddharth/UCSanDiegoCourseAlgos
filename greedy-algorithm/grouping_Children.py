# Many children came to a celebration. Organize them into the minimum possible number of groups such that the age of any two children in the same group differ by at most one year.

def makeGroup(childrenList):
    childrenList.sort()
    start = 0
    end = 0
    newList = []
    while end < len(childrenList):

        if childrenList[end] - childrenList[start] > 1:
            newList.append(childrenList[start:end])
            start = end

        if end == len(childrenList)-1:
            newList.append([childrenList[end]])
        end += 1

    print(newList)


makeGroup([1, 5, 6, 7, 2, 6, 9])
makeGroup([4, 8, 6, 5, 9, 55, 2, 37])
makeGroup([12, 15, 14, 13, 16, 18, 14, 14, 15, 13, 19])
makeGroup([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 14, 15, 1, 5, 15, 15])
