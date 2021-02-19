# Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
# pylint: disable=unused-variable

def ffib(n):
    f1 = 0
    f2 = 1
    if n == 1:
        return f1
    elif n == 2:
        return f2
    else:
        for x in range(2, n):
            fTemp = f2
            f2 = f1+f2
            f1 = fTemp
            # print("in " + str(x) + " ftemp is " + str(fTemp) +
            #       ", f1 is " + str(f1) + ", f2 is " + str(f2))

    return f2


if __name__ == "__main__":
    print(ffib(101))
