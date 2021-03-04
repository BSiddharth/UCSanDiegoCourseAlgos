# 2021-03-04-17-01-39.png

def maxNumberOfChildren(n):
    sum = 0
    count = 1
    prizeList = []
    while sum < n:
        prizeList.append(count)
        sum += count
        count += 1
    if sum == n:
        print(f"Maximum number of kids can be {len(prizeList)}")
        print("The awards will be like this from 1st position to last",
              list(reversed(prizeList)))
    else:
        for _ in range(2):
            sub = prizeList.pop()
            sum -= sub
        prizeList.append(n-sum)
        print(f"Maximum number of kids can be {len(prizeList)}")
        print("The awards will be like this from 1st position to last",
              list(reversed(prizeList)))


if __name__ == '__main__':
    maxNumberOfChildren(10)
    maxNumberOfChildren(45)
    maxNumberOfChildren(26)
    maxNumberOfChildren(18)
