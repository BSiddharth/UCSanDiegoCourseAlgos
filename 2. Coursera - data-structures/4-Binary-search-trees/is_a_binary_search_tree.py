# 2021-05-22-17-03-11.png

# I am given a tree and I need to find if its a BST
# i use list based queues and stack to save time but sometimes linked list is better
# if we do an inOrder traversal of the tree , it should be in ascending order to be a bst

from binary_tree_traversals import Node


def inOrder(bTreeNode, l):
    # print(bTreeNode, end=" ")

    if bTreeNode.left != None:
        inOrder(bTreeNode.left, l)

    l.append(bTreeNode)

    if bTreeNode.right != None:
        inOrder(bTreeNode.right, l)
    return l


def is_bst(bTreeRoot):

    returnList = inOrder(bTreeRoot, [])
    for x in range(len(returnList)-1):
        if returnList[x].key > returnList[x+1].key:
            print(False)
            return
    print(True)


if __name__ == "__main__":
    firstTree = Node(4)
    firstTree.left = Node(2)
    firstTree.right = Node(5)
    firstTree.left.left = Node(1)
    firstTree.left.right = Node(7)
    is_bst(firstTree)  # false
    firstTree = Node(4)
    firstTree.left = Node(2)
    firstTree.right = Node(5)
    firstTree.left.left = Node(1)
    firstTree.left.right = Node(3)
    is_bst(firstTree)  # true
