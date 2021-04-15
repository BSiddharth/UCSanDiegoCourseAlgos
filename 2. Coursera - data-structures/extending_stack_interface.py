from basicDS import DoubleNode, DoubleLinkedList
import math


class MaxStack():
    def __init__(self, dNode):
        self.internalDoubleLinkedList = DoubleLinkedList(dNode)
        self.max = dNode
        self.maxDoubleLinkedList = DoubleLinkedList(DoubleNode(self.max.key))

    def push(self, dNode):
        self.internalDoubleLinkedList.addAtEnd(dNode)
        self.max = max(self.max, dNode)
        self.maxDoubleLinkedList.addAtEnd(DoubleNode(self.max.key))

    def remove(self):
        self.internalDoubleLinkedList.removeFromEnd()
        if self.maxDoubleLinkedList.head == None:
            self.max = DoubleNode(-math.inf)
        else:
            self.maxDoubleLinkedList.removeFromEnd()
            self.max = self.maxDoubleLinkedList.tail

    def getMax(self):
        print(self.max)

    # def __init__(self, nodeList=[]):
    #     super().__init__(nodeList=[])
    #     self.maxLinkedList = LinkedList()
    #     self.max = Node(-math.inf)

    #     for node in nodeList:
    #         self.max = max(self.max, node)
    #         self.maxLinkedList.addAtLast(self.max)

    # def push(self, node):
    #     super().push(node)
    #     self.max = max(self.max, node)
    #     self.maxLinkedList.addAtLast(Node(self.max.key))
    #     print(self.maxLinkedList.tail, "push se aarha hoo")

    #     # if self.max == None:
    #     #     self.max = node
    #     # else:
    #     #     self.max = max(self.max, node)

    # def remove(self):
    #     super().remove()
    #     self.maxLinkedList.popFromLast()
    #     print(self.maxLinkedList.tail, "remove se aarha hoo")

    # def getMax(self):
    #     print(self.maxLinkedList.tail)

    def printMaxList(self):
        node = self.maxDoubleLinkedList.head
        if node == None:
            print('empty list')
        else:
            while node != None:
                print(node, end=" ")
                node = node.next
            print()

    def printList(self):
        node = self.internalDoubleLinkedList.head
        if node == None:
            print('empty list')
        else:
            while node != None:
                print(node, end=" ")
                node = node.next
            print()


if __name__ == '__main__':
    maxStack = MaxStack(DoubleNode(1))
    # maxStack.push(DoubleNode(1))
    maxStack.push(DoubleNode(7))
    maxStack.getMax()
    maxStack.remove()
    maxStack.getMax()
