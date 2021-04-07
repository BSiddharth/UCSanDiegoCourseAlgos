from basicDS import Stack, Node


def checkBrackets(string):
    bracketDict = {'[': ']', '{': '}', '(': ')'}
    brackets = ('[', ']', '{', '}', '(', ')')
    li = list(string.split())
    stack = Stack()
    for x in range(len(li)):
        if li[x] in brackets:
            if li[x] in ("]", '}', ')'):

                if bracketDict[stack.tail.key] == li[x]:
                    stack.remove()
                elif bracketDict[stack.tail.key] != li[x]:
                    print(
                        f"Here is the error at {x+1}, {li[x]} does not have an opening bracket")
                    return

            else:
                stack.push(Node(li[x]))
    if stack.length != 0:
        print('You are missing a closing bracket')
        return
    print('All good boi')


if __name__ == '__main__':
    checkBrackets('[]')
    checkBrackets('{}[]')
    checkBrackets('{()}')
    checkBrackets('(())')
    checkBrackets('{[]}()')
    checkBrackets('{')
    checkBrackets('{[]}()')
    checkBrackets('{[]}()')
    checkBrackets('{[}')
    checkBrackets('foo(bar);')
    checkBrackets('foo(bar[i);')
