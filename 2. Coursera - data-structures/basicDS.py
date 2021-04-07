class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self, nodeList=[]):
        if nodeList == None:
            self.head = None
            self.tail = None
            self.length = 0
        self.head = nodeList[0]
        self.tail = nodeList[-1]
        self.length = len(nodeList)
        if len(nodeList) >= 1:
            for x in range(len(nodeList)):
                if x+1 <= len(nodeList):
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
        else:
            pointer = self.head
            while pointer.next.next != None:
                pointer = pointer.next
            self.tail = pointer
            pointer.next == None
        self.length -= 1


class Stack:
    def __init__(self, *nodeList):
        self.internalLinkedList = LinkedList(nodeList)
        self.tail = self.internalLinkedList.tail
        self.length = self.internalLinkedList.length

    def push(self, node):
        self.internalLinkedList.addAtLast(node)

    def remove(self):
        self.internalLinkedList.popFromLast()
