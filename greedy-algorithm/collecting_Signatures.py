# 2021-03-03-01-36-41.png

def findMinContact(pairList):
    pairList.sort()
    start = pairList[0][0]
    end = pairList[0][1]
    contact = 1
    contactlist = [start]
    for x in range(len(pairList)):
        if (pairList[x][0] <= end) & (pairList[x][1] <= end):

            end = pairList[x][1]
            start = pairList[x][0]
            contactlist.pop()
            contactlist.append(start)

        elif pairList[x][0] <= end:
            start = pairList[x][0]
            contactlist.pop()
            contactlist.append(start)

            continue
        else:
            contact += 1

            end = pairList[x][1]
            start = pairList[x][0]

            contactlist.append(start)

    print(contact)
    print(contactlist)


if __name__ == '__main__':
    findMinContact([[1, 3],  [3, 6], [2, 5]])
    findMinContact([(4, 7), (2, 2), (1, 3), (3, 4)])
    findMinContact([(4, 7), (2, 5), (1, 3), (5, 6)])
    findMinContact([(10, 20), (12, 25), (20, 30)])
    findMinContact([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)])
