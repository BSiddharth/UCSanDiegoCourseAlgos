# Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
# Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
# Constraints. 1 ≤ 𝑛 ≤ 1018, 2 ≤ 𝑚 ≤ 103.
# Output Format. Output 𝐹𝑛 mod 𝑚.

# key to solve this with best method is to know that for any integer 𝑚 ≥ 2, the sequence 𝐹𝑛 mod 𝑚 is periodic. The period always starts with 01 and is known as Pisano period.

# pylint: disable=unused-variable

from find_the_n_fibonacci import ffib


def findMODeasyWay(n, m):
    return ffib(n) % m


def findMODbestWay(n, m):
    patternList = []

    f1 = 0
    f2 = 1
    if n == 1:
        return f1
    elif n == 2:
        return f2
    patternList.extend([f1, f2])

    for index in range(2, n):
        fTemp = f2
        f2 = (f1+f2) % m
        f1 = fTemp
        if f2 != 0:
            patternList.append(f2)
        else:
            if (f1+f2) % m != 1:
                patternList.append(f2)
            else:
                break

    if len(patternList) < n:
        indexToLook = n % len(patternList)
        # print("indexToLook: " + str(indexToLook))
        # print("length of  list is " + str(len(patternList)))
        # print("list is " + str(patternList))
        return patternList[indexToLook-1]
    else:
        # print("length of  list is " + str(len(patternList)))
        # print("list is " + str(patternList))
        return patternList[-1]


if __name__ == "__main__":
    print(findMODeasyWay(240, 1000))
    print(findMODbestWay(240, 1000))

    print(findMODeasyWay(300, 239))
    print(findMODbestWay(300, 239))

    print(findMODeasyWay(560, 239))
    print(findMODbestWay(560, 239))

    print(findMODeasyWay(630, 896))
    print(findMODbestWay(630, 896))

    # this is will take bhot zyada time even when its linear
    print(findMODeasyWay(2816213589, 239))
    # thats why this is the best way
    print(findMODbestWay(2816213589, 239))
