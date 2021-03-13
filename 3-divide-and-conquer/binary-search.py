# 2021-03-13-19-56-39.png

def binarySearch(sortedList, number):
    sortedList.sort()
    print(f"the list to be searched is {sortedList}")

    for n in number:
        print(f'the number to be searched is {n}')

        low = 0
        high = len(sortedList) - 1
        found = False

        while low != high-1:
            mid = (low + high)//2

            # print('low is ' + str(low))
            # print('high is ' + str(high))
            # print('mid is ' + str(mid))

            if sortedList[low] == n:
                print('The index is ' + str(low))
                found = True
                break

            if sortedList[high] == n:
                print('The index is ' + str(high))
                found = True
                break

            if sortedList[mid] == n:
                print('The index is ' + str(mid))
                found = True
                break
            if sortedList[mid] > n:
                high = mid

            if sortedList[mid] < n:
                low = mid
        if not found:
            if sortedList[low] == n:
                print('The index is ' + str(low))
                found = True

            if sortedList[high] == n:
                print('The index is ' + str(high))
                found = True

        if not found:
            print('Number not found')


if __name__ == '__main__':
    binarySearch([5, 1, 5, 8, 12, 13], [5, 8, 1, 23, 1, 11])
