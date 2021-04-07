class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class LinkedList:
    def __init__(self, nodeList=[]):
        if len(nodeList) == 0:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = nodeList[0]
            self.tail = nodeList[-1]
            self.length = len(nodeList)
        if len(nodeList) >= 1:
            for x in range(len(nodeList)):
                if x+1 <= len(nodeList)-1:
                    nodeList[x].next = nodeList[x+1]
                else:
                    nodeList[x].next = None

    def addAtLast(self, node):
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            node.next = None
        self.length += 1

    def popFromLast(self):

        if self.head.next == None:
            self.head = None
            self.tail = None
            self.length = 0
            return
        else:
            pointer = self.head
            while pointer.next.next != None:
                pointer = pointer.next
            self.tail = pointer
            pointer.next == None
        self.length -= 1


class Stack:
    def __init__(self, nodeList=[]):
        self.internalLinkedList = LinkedList(nodeList)
        self.head = self.internalLinkedList.head
        self.tail = self.internalLinkedList.tail
        self.length = self.internalLinkedList.length

    def push(self, node):
        self.internalLinkedList.addAtLast(node)
        self.length = self.internalLinkedList.length

    def remove(self):
        self.internalLinkedList.popFromLast()
        self.length = self.internalLinkedList.length


if __name__ == '__main__':

    stack = Stack([
        # Node(0),
        # Node(1),
        # Node(2),
        # Node(3),
    ])

    print(stack.length)
    print(stack.head)
    print(stack.tail)
    stack.push(Node(4))
    print(stack.length)
    print(stack.head)
    print(stack.tail)
    stack.remove()
    print(stack.length)
    print(stack.head)
    print(stack.tail)
