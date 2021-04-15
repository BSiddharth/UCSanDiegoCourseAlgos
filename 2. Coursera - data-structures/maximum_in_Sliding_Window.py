# 2021-04-15-10-12-30.png
from basicDS import DoubleNode, DoubleLinkedList


def maxSlidingWindow(l, w):
    n = len(l)
    dLinkedList = DoubleLinkedList(l[0])
    for x in range(1, w):
        dNode = DoubleNode(l[x])
        # dLinkedList.addAtLast()


if __name__ == '__main__':
    dlist = DoubleLinkedList(DoubleNode(1))
    dlist.addAtEnd(DoubleNode(2))
    dlist.addAtEnd(DoubleNode(3))
    dlist.addAtEnd(DoubleNode(4))
    dlist.removeFromEnd()
    dlist.removeFromEnd()
    dlist.removeFromEnd()
    dlist.removeFromEnd()
