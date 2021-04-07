from basicDS import Stack, Node


def checkBrackets(string):
    bracketDict = {'[': ']', '{': '}', '(': ')'}
    brackets = ('[', ']', '{', '}', '(', ')')
    li = list(string)
    indexList = []
    stack = Stack()
    for x in range(len(li)):
        if li[x] in brackets:
            indexList.append(x)
            if li[x] in ("]", '}', ')'):
                if stack.length == 0:
                    print(
                        f"Here is the error at {indexList[-1]+1}, {li[indexList[-1]]} does not have an opening bracket")

                if bracketDict[stack.tail.key] == li[x]:
                    stack.remove()
                elif bracketDict[stack.tail.key] != li[x]:
                    print(
                        f"Here is the error at {indexList[-2]+1}, {li[indexList[-2]]} does not have an closing bracket")
                    return

            else:
                stack.push(Node(li[x]))
    if stack.length != 0:
        print(
            f"Here is the error at {indexList[-1]+1}, {li[indexList[-1]]} does not have an closing bracket")

    print('All good boi')


if __name__ == '__main__':
    checkBrackets('[]')

    checkBrackets('{')
    checkBrackets('{}[')
    checkBrackets('{[}')
    checkBrackets('foo(bar);')
    checkBrackets('foo(bar[i);')
