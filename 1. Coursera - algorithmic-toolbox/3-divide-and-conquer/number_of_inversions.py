# 2021-03-17-19-29-58.png


def findNumOfInversions(arr):
    n = len(arr)
    tmp = [0]*n
    inv = _findNumOfInversions(arr, tmp, 0, n-1)
    print(inv)


def _findNumOfInversions(arr, tmp, left, right):
    inv = 0
    if left < right:
        mid = (left + right)//2
        inv += _findNumOfInversions(arr, tmp, left, mid)
        inv += _findNumOfInversions(arr, tmp, mid+1, right)

        inv += merge(arr, tmp, left, mid, right)
    return inv


def merge(arr, tmp, left, mid, right):
    inv = 0
    i = left
    k = left
    j = mid+1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            inv += (mid - i+1)
            tmp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        tmp[k] = arr[j]
        k += 1
        j += 1
    for index in range(left, right+1):
        arr[index] = tmp[index]
    return inv


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    # arr = [2, 3, 9, 2, 9]

    findNumOfInversions(arr)
