# 2021-04-15-10-12-30.png
from basicDS import DoubleNode, DoubleLinkedList


def maxSlidingWindow(l, w):
    n = len(l)
    dLinkedList = DoubleLinkedList(DoubleNode(l[0]))
    for x in range(1, w):
        while l[x] > dLinkedList.head.key:
            dLinkedList.removeFromStart()
            if dLinkedList.head == None:
                break
        dLinkedList.addAtStart(DoubleNode(l[x]))
    print("list here at step 1 is", end=" ")
    dLinkedList.printList()
    print("The max in the list is", dLinkedList.tail)

    for x in range(w, n):
        if l[x-w] == dLinkedList.tail.key:
            dLinkedList.removeFromEnd()
            print(dLinkedList.head.key, "is being thrown out step", x-w+2)
        while l[x] > dLinkedList.head.key:
            print("comparing", l[x], "and",
                  dLinkedList.head.key, "in step", x-w+2)
            print(dLinkedList.head.key, 'removed', 'in step', x-w+2)

            dLinkedList.removeFromStart()
            if dLinkedList.head == None:
                print("empty list in step", x-w+2)
                break
        dLinkedList.addAtStart(DoubleNode(l[x]))
        print("The max in the list is", dLinkedList.tail)
        print("list here in step", x-w+2, "is", end=" ")
        dLinkedList.printList()


if __name__ == '__main__':
    maxSlidingWindow([2, 7, 3, 1, 5, 2, 6, 2, ], 4)
