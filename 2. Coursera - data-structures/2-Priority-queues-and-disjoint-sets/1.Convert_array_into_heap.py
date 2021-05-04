
def shftDown(pos, swapPos, arr):
    arr[pos-1], arr[(swapPos) - 1] = arr[(swapPos)-1], arr[pos-1]
    print(pos, swapPos)


def shftUp(pos, arr):
    if pos//2 == 0:
        # assert (
        #     pos/2)-1 >= 0, "This node is already at the root position and can't be shifted up"
        if (pos/2)-1 >= 0:
            arr[pos-1], arr[(pos/2)-1] = arr[(pos/2)-1], arr[pos-1]
            print(pos, pos/2)

    else:
        # assert (
        #     (pos-1)/2)-1 >= 0, "This node is already at the root position and can't be shifted up"
        if ((pos-1)/2)-1 >= 0:
            arr[pos-1], arr[((pos-1)/2)-1] = arr[((pos-1)/2)-1], arr[pos-1]
            print(pos, (pos-1)/2)


# def remove(pos):
#     assert pos <= len(arr), 'Pos is out of bound'
#     arr[pos-1], arr[len(arr)-1] = arr[len(arr)-1], arr[pos-1]


def makeHeap(arr):
    numberOfSwaps = 0
    x = 1
    for y in range(len(arr)):
        while x-1 <= len(arr):
            if 2*x <= len(arr):
                while arr[x - 1] > arr[2*x-1] or arr[x-1] > arr[2*x]:
                    if arr[x - 1] > arr[2*x-1]:
                        shftDown(x, 2*x, arr)
                    else:
                        shftDown(x, (2*x)+1, arr)

                    numberOfSwaps += 1

            x += 1
        x = 1
    print(numberOfSwaps)


if __name__ == '__main__':
    makeHeap([5, 4, 3, 2, 1])
    makeHeap([1, 2, 3, 4, 5])
