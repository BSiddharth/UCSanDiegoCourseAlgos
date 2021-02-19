# Problem Description
# Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 107.
# Output Format. Output the last digit of 𝐹𝑛.

# pylint: disable=unused-variable


def lastDigitFinder(n):
    # just like finding nth fibonacci but store mod 10 / last digit of every number.
    # for best way see fibonacci_Number_Again

    f1 = 0
    f2 = 1
    if n == 1:
        return f1
    elif n == 2:
        return f2
    else:
        for x in range(2, n):
            fTemp = f2 % 10
            f2 = (f1+f2) % 10
            f1 = fTemp
            # print("in " + str(x) + " ftemp is " + str(fTemp) +
            #       ", f1 is " + str(f1) + ", f2 is " + str(f2))

    return f2


print(lastDigitFinder(332))
