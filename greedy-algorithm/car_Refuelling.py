# Input: A car which can travel at most L kilometers with full tank, a source point A, a destination point B and n gas stations at distances x1 ≤ x2 ≤ x3 ≤ · · · ≤ xn in kilometers from A along the path from A to B.

# Output: The minimum number of refills to get from A to B, besides refill at A.

def minNumOfRefills(L, Xlist):

    Xlist.insert(0, 0)
    currentNumOfRefills = 0
    maxDistance = L
    # currentPos = 0

    for i in range(len(Xlist)-1):
        if maxDistance - (Xlist[i+1] - Xlist[i]) >= 0:
            maxDistance -= (Xlist[i+1] - Xlist[i])
        else:
            currentNumOfRefills += 1
            maxDistance = L
            if maxDistance - (Xlist[i+1] - Xlist[i]) < 0:
                print("Not Possible")
                return
            else:
                maxDistance -= (Xlist[i+1] - Xlist[i])

    print(currentNumOfRefills)


if __name__ == "__main__":
    minNumOfRefills(1, [1, 2, 3, 4, 5, 6])  # 5
    minNumOfRefills(2, [1, 2, 3, 4, 5, 6])  # 2
    minNumOfRefills(3, [1, 2, 3, 4, 5, 6])  # 1
    minNumOfRefills(400, [200, 375, 550, 750, 950])  # 2
    minNumOfRefills(100, [60, 150, 469, 660, 710, 820])  # NP
    minNumOfRefills(200, [60, 150, 310, 469, 660, 710, 820])  # 4
