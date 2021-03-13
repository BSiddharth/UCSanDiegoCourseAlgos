# Task. Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
# Input Format. The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space.
# Constraints. 0 ≤ 𝑚 ≤ 𝑛 ≤ 1018.
# Output Format. Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.

from Last_Digit_of_the_Sum_of_Fibonacci_Numbers import lastDigitOfsumOfFibBest


def lastDigitOfPartialSumOfFibBest(m, n):
    result = lastDigitOfsumOfFibBest(n) - lastDigitOfsumOfFibBest(m-1)
    if result < 0:
        return 10 + result
    else:
        return result


if __name__ == '__main__':
    print(lastDigitOfPartialSumOfFibBest(1000, 1003))
    print(lastDigitOfPartialSumOfFibBest(11, 1000))
    print(lastDigitOfPartialSumOfFibBest(526, 895))
