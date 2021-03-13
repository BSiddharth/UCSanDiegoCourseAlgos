# Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
# Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2·10^9.
# Output Format. Output the least common multiple of 𝑎 and 𝑏.

# The key to solving this problem is knowing that a x b = LCM(a, b) * GCD (a, b)

from greatest_Common_Divisor import findGCD


def findLCM(a, b):
    return a*b/findGCD(a, b)


print(findLCM(28851538, 1183019))
