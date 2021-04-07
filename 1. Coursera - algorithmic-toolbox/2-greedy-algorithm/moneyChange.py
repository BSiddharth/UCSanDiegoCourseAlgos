# Task. The goal in this problem is to find the minimum number of coins needed to change the input value  (an integer) into coins with denominations 1, 5, and 10.
# Input Format. The input consists of a single integer 𝑚.
# Constraints. 1 ≤ 𝑚 ≤ 103.
# Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.


def numOfCoins(m):
    balance = m
    coinList = [10, 5, 1]

    for x in range(len(coinList)):
        currentCoin = coinList[x]
        coinList[x] = balance//currentCoin
        balance -= currentCoin*coinList[x]

    print(coinList)


if __name__ == '__main__':
    numOfCoins(15)
    numOfCoins(36)
    numOfCoins(64)
    numOfCoins(50)
