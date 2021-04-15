from basicDS import Stack, Node, LinkedList
import math


class MaxStack(Stack):
    def __init__(self, nodeList=[]):
        super().__init__(nodeList=[])
        self.maxLinkedList = LinkedList()
        self.max = Node(-math.inf)

        for node in nodeList:
            self.max = max(self.max, node)
            self.maxLinkedList.addAtLast(self.max)

    def push(self, node):
        super().push(node)
        self.max = max(self.max, node)
        self.maxLinkedList.addAtLast(Node(self.max.key))
        print(self.maxLinkedList.tail, "push se aarha hoo")

        # if self.max == None:
        #     self.max = node
        # else:
        #     self.max = max(self.max, node)

    def remove(self):
        super().remove()
        self.maxLinkedList.popFromLast()
        print(self.maxLinkedList.tail, "remove se aarha hoo")

    def getMax(self):
        print(self.maxLinkedList.tail)

    def printMaxList(self):
        node = self.maxLinkedList.head
        while node.next != None:
            print(node, end=" ")
            node = node.next
        print(node)

    def printList(self):
        node = self.internalLinkedList.head
        while node.next != None:
            print(node, end=" ")
            node = node.next
        print(node)


if __name__ == '__main__':
    maxStack = MaxStack()
    maxStack.getMax()
    maxStack.push(Node(1))
    maxStack.push(Node(4))
    maxStack.push(Node(3))
    maxStack.push(Node(2))
    maxStack.printList()
    maxStack.printMaxList()
    maxStack.getMax()
    maxStack.remove()
    maxStack.remove()
    maxStack.printMaxList()
    maxStack.printList()
    maxStack.remove()
    maxStack.getMax()
    maxStack.remove()
    maxStack.getMax()

    # bug hai. mujhe nya double node vali linked list and stack bnana pdega bhot alaas hai toh nhi kar rha but aagya hai ye samaj sab done hai
