# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

# Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.

# its power of 10

# Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑊 ≤ 2 · 106
# 0 ≤ 𝑣𝑖 ≤ 2 · 106, 0 < 𝑤𝑖 ≤ 2 · 106 for all 1 ≤ 𝑖 ≤ 𝑛. All the numbers are integers.

# Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the difference between the answer of your program and the optimal value should be at most 10−3. To ensure this, output your answer with at least four digits after the decimal point(otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

def maxVal(valueList, weightList, maxWeight):
    valuePercentList = []
    maxValue = 0
    for x in range(len(valueList)):
        valuePercentList.append(valueList[x]/weightList[x])

    unorderedDataDict = {}
    for x in range(len(valueList)):
        unorderedDataDict[valuePercentList[x]] = weightList[x]
    orderedDataDict = {k: unorderedDataDict[k]
                       for k in sorted(unorderedDataDict, reverse=True)}
    weightList = list(orderedDataDict.values())
    keyList = list(orderedDataDict.keys())
    # print(orderedDataDict)
    # print(keyList)
    # print(weightList)

    unorderedDataDict.clear()
    for x in range(len(orderedDataDict)):
        p = maxWeight/(weightList[x]) if maxWeight/(weightList[x]) <= 1 else 1
        maxValue += p*weightList[x]*keyList[x]
        maxWeight -= p*weightList[x]
        if maxWeight == 0:
            break

    print(maxValue)


if __name__ == '__main__':

    maxVal([30, 20, 100, 90, 60], [5, 10, 20, 30, 40], 60)
