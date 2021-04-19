class Node:
    def __init__(self, key=0):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)

    def __gt__(self, other):
        return self.key > other.key


class DoubleNode:
    def __init__(self, key=0):
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.key)

    def __gt__(self, other):
        return self.key > other.key


class DoubleLinkedList:
    def __init__(self, dNode):
        self.head = dNode
        self.tail = dNode
        self.length = 1

    def addAtEnd(self, dNode):
        if self.head == None:
            self.head = dNode
            self.tail = dNode
        else:
            self.tail.next = dNode
            dNode.prev = self.tail
            self.tail = dNode
        self.length += 1

    def removeFromEnd(self):
        assert self.head != None, "Can't remove element from an empty list"
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

    def removeFromStart(self):
        assert self.head != None, "Can't remove element from an empty list"
        self.head = self.head.next
        # self.tail = self.tail.prev
        self.length -= 1

    def addAtStart(self, dNode):
        if self.head == None:
            self.head = dNode
            self.tail = dNode
        else:
            self.head.prev = dNode
            dNode.next = self.head
            self.head = dNode
        self.length += 1

    def printList(self):
        node = self.head
        if node == None:
            print('empty list')
        else:
            while node != None:
                print(node, end=" ")
                node = node.next
            print()


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

        if self.head.next == None or self.head == None:
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
        self.head = self.internalLinkedList.head
        self.tail = self.internalLinkedList.tail
        self.length = self.internalLinkedList.length

    def remove(self):
        self.internalLinkedList.popFromLast()
        self.head = self.internalLinkedList.head
        self.tail = self.internalLinkedList.tail
        self.length = self.internalLinkedList.length


# class TreeNode:
#     def __init__(self, value=0, children=[]):
#         self.value = value
#         self.children = children


# class Tree:
#     def __init__(self, root):
#         self.root = root


class Queue:
    def __init__(self, first):
        self.first = first
        self.last = first
        self.length = 1

    def addAtLast(self, dNode):
        if self.length == 0:
            self.first = dNode
            self.last = dNode
        else:
            dNode.next = self.last
            self.last.prev = dNode
            self.last = dNode
        self.length += 1

    def popFirst(self):
        self.first = self.first.prev
        if self.length > 1:
            self.first.next.prev = None
            self.first.next = None
        else:
            self.last = None

        self.length -= 1


if __name__ == '__main__':
    d = DoubleLinkedList(DoubleNode(1))
    d.addAtEnd(DoubleNode(2))
    d.addAtEnd(DoubleNode(5))
    d.addAtEnd(DoubleNode(8))
    d.addAtEnd(DoubleNode(6))
    d.printList()
    # stack = Stack([
    #     # Node(0),
    #     # Node(1),
    #     # Node(2),
    #     # Node(3),
    # ])

    # print(stack.length)
    # print(stack.head)
    # print(stack.tail)
    # stack.push(Node("o"))
    # print(stack.length)
    # print(stack.head)
    # print(stack.tail)
    # stack.remove()
    # print(stack.length)
    # print(stack.head)
    # print(stack.tail)
