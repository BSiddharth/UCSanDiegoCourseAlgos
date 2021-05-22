# same as prev one but it can contain same elements. Duplicate can only be right child

from binary_tree_traversals import Node


def inOrder(bTreeNode, l):

    if bTreeNode.left != None:
        if bTreeNode.left.key == bTreeNode.key:
            return False
        inOrder(bTreeNode.left, l)

    l.append(bTreeNode)

    if bTreeNode.right != None:
        inOrder(bTreeNode.right, l)
    return l


def is_bst(bTreeRoot):

    returnList = inOrder(bTreeRoot, [])
    if returnList == False:
        print(False)
        return

    for x in range(len(returnList)-1):
        if returnList[x].key > returnList[x+1].key:
            print(False)
            return
    print(True)


if __name__ == '__main__':
    firstTree = Node(2)
    firstTree.left = Node(2)
    firstTree.right = Node(3)

    is_bst(firstTree)
    firstTree = Node(2)
    firstTree.left = Node(1)
    firstTree.right = Node(2)

    is_bst(firstTree)
    firstTree = Node(4)

    is_bst(firstTree)
