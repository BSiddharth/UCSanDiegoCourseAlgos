# Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
# Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2·10^9.
# Output Format. Output GCD(𝑎, 𝑏).

# here we are using Euclidean algorithm for computing the greatest common divisor

def findGCD(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    else:
        return findGCD(b, a % b)


if __name__ == '__main__':
    print(findGCD(28851538, 1183019))
    print(findGCD(18, 35))
