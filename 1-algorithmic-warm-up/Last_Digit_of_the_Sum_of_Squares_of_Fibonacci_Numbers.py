# Task. Compute the last digit of 𝐹20 + 𝐹21 + · · · + 𝐹2𝑛.
# Input Format. Integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 1018.
# Output Format. The last digit of 𝐹20 + 𝐹21 + · · · + 𝐹2𝑛.

# key to solve this problem is knowing that f(n)^2 = f(n)*f(n+1)

from fibonacci_Number_Again import findMODbestWay


def findLastDigitOfTheSumOfSquaresOfFibonacciNumbers(n):
    return (findMODbestWay(n, 10)*findMODbestWay(n+1, 10)) % 10


if __name__ == '__main__':
    print(findLastDigitOfTheSumOfSquaresOfFibonacciNumbers(8))
    print(findLastDigitOfTheSumOfSquaresOfFibonacciNumbers(74))
    print(findLastDigitOfTheSumOfSquaresOfFibonacciNumbers(1234567891))
