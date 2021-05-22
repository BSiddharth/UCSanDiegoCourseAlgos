# 2021-05-22-12-56-38.png

# I will have a binary tree and I need to traverse it in all three ways. I can do this without recursios but I cant import DS cuz of the name that I have chosen

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.key)


def inOrder(bTreeNode):
    if bTreeNode.left != None:
        inOrder(bTreeNode.left)

    print(bTreeNode, end=" ")

    if bTreeNode.right != None:
        inOrder(bTreeNode.right)


def preOrder(bTreeNode):
    print(bTreeNode, end=" ")

    if bTreeNode.left != None:
        preOrder(bTreeNode.left)

    if bTreeNode.right != None:
        preOrder(bTreeNode.right)


def postOrder(bTreeNode):

    if bTreeNode.left != None:
        postOrder(bTreeNode.left)

    if bTreeNode.right != None:
        postOrder(bTreeNode.right)

    print(bTreeNode, end=" ")


def traverse3(bTreeNode):
    print("with recursion", end=" ")
    inOrder(bTreeNode)
    print("")
    print("with recursion", end=" ")
    preOrder(bTreeNode)
    print("")
    print("with recursion", end=" ")
    postOrder(bTreeNode)
    print('')


if __name__ == "__main__":
    firstTree = Node(4)
    firstTree.left = Node(2)
    firstTree.right = Node(5)
    firstTree.left.left = Node(1)
    firstTree.left.right = Node(3)
    traverse3(firstTree)
    firstTree = Node(0)
    firstTree.left = Node(70)
    firstTree.right = Node(20)
    firstTree.right.right = Node(60)
    firstTree.right.right.left = Node(10)
    firstTree.left.left = Node(50)
    firstTree.left.right = Node(40)
    firstTree.left.right.left = Node(30)
    firstTree.left.right.left.left = Node(80)
    firstTree.left.right.left.right = Node(90)
    traverse3(firstTree)
