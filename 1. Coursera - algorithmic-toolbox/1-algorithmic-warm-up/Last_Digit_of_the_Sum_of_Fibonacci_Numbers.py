# Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 1018.
# Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.

# pylint: disable=unused-variable

# best way to solve is knowing that sum till nth fib = (n-2)th fib - 1. https://thisthread.blogspot.com/2018/02/last-digit-of-sum-of-fibonacci-numbers.html
from fibonacci_Number_Again import findMODbestWay


def lastDigitOfsumOfFibEasy(n):
    f1 = 0
    f2 = 1
    fsum = 1
    if n == 1:
        return f1 % 10
    elif n == 2:
        return (f1+f2) % 10
    else:
        for x in range(2, n):
            f1, f2 = f2, (f1+f2) % 10
            fsum = (fsum + f2) % 10

    return fsum


def lastDigitOfsumOfFibBest(n):
    # to fix the bug in line 45
    result = findMODbestWay(n+2, 10) - 1
    if result == -1:
        result = 9
    return result


if __name__ == "__main__":
    print(lastDigitOfsumOfFibEasy(4))
    print(lastDigitOfsumOfFibBest(4))

    print(lastDigitOfsumOfFibEasy(101))
    print(lastDigitOfsumOfFibBest(101))

    print(lastDigitOfsumOfFibEasy(569))

    # here -1 aarha hai. 9 aana chaiye but ye bug hai 0-1 = -1 hai isiliye ye hogya. Bug fixed in line 30
    print(lastDigitOfsumOfFibBest(569))

    print(lastDigitOfsumOfFibEasy(50000000))
    print(lastDigitOfsumOfFibBest(50000000))
