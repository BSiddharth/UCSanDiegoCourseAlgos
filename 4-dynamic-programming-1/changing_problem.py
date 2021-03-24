# as you can see in the example given in the course greedy algo is not always optimal so we use dynamic programming to solve the change problem
# https://www.youtube.com/watch?v=jgiZlGzXMBw this helped.

def dpChange(change, coins):
    coins.sort()
    minValue = coins[0]
    defaultNum = (change//minValue) + 10
    changeList = [defaultNum]*(change+1)
    changeList[0] = 0

    for x in range(change+1):
        mincoins = changeList[x]
        for y in coins:
            if x >= y:
                mincoins = min(mincoins, changeList[x-y]+1)
            changeList[x] = mincoins
    print("Not possible" if changeList[-1] == defaultNum else changeList[-1])


if __name__ == "__main__":
    dpChange(9, [1, 6, 5])
    dpChange(40, [5, 20, 30])
    dpChange(11, [1, 2, 5])
    dpChange(11, [10, 2, 50])
