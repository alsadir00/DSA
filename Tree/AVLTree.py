
# 1. What is an AVL Tree?

#     An AVL Tree is a self-balancing Binary Search Tree (BST).
#     For every node, the balance factor is maintained as:
#     Balance Factor=Height(left subtree)−Height(right subtree)
#     The balance factor can only be –1, 0, or +1.

# If this condition is violated after an insertion or deletion, the tree is rebalanced using rotations.

# 2. Why AVL Tree?
#     AVL trees are used to keep the BST balanced, which ensures:
#     Fast search, insertion, and deletion
#     Prevents the BST from becoming skewed (like a linked list) which makes the search operation of time complexity o(n)
#     Guarantees O(log n) time complexity for major operations
#     Without balancing, a BST can degrade to O(n) time.

# 3. Common Operations in AVL Tree
#     Insertion
#         Insert like a normal BST
#         Update heights and balance factors
#         Perform rotations if unbalanced

#     Deletion
#         Delete like a BST
#         Rebalance the tree if needed

#     Searching
#         Same as BST
#         Time complexity: O(log n)

#     Rotations (Rebalancing)
#         LL Rotation
#         RR Rotation
#         LR Rotation
#         RL Rotation

#     Traversal
#         Inorder
#         Preorder
#         Postorder

# 4. Advantages of AVL Tree
#     Always balanced
#     Faster lookup than unbalanced BST
#     Predictable performance

# 5. Disadvantages
#     More complex to implement
#     Extra overhead for rotations
#     Slightly slower insert/delete than Red-Black Trees
# # operations to perform in AVL tree


#  this is for the level traversal
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)

def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)

def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)

def search(rootNode, value):
    if rootNode.data == value:
        print("The value is found")
    elif value < rootNode.data:
        if rootNode.left.data == value:
            print("The value is found")
        else:
            search(rootNode.left, value)
    else:
        if rootNode.right.data == value:
            print("The value is found")
        else:
            search(rootNode.right, value)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(unbalancedNode):
    newRoot = unbalancedNode.left
    unbalancedNode.left = unbalancedNode.left.right
    newRoot.right = unbalancedNode
    unbalancedNode.height = 1 + max(getHeight(unbalancedNode.left), getHeight(unbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot

def leftRotate(unbalancedNode):
    newRoot = unbalancedNode.right
    unbalancedNode.right = unbalancedNode.right.left
    newRoot.left = unbalancedNode
    unbalancedNode.height = 1 + max(getHeight(unbalancedNode.left), getHeight(unbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)


def insert(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left = insert(rootNode.left, nodeValue)
    else:
        rootNode.right = insert(rootNode.right, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.left.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.right.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.left is None:
        return rootNode
    return getMinValueNode(rootNode.left)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        elif rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.left) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.right) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.left) < 0:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.right) > 0:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    
    return rootNode


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "The AVL has been successfully deleted"

newAvl = AVLNode(5)
newAvl = insert(newAvl, 10)
newAvl = insert(newAvl, 15)
newAvl = insert(newAvl, 20)
newAvl = insert(newAvl, 30)
levelOrder(newAvl)
newAvl = deleteNode(newAvl, 10)
print('=' * 30)
levelOrder(newAvl)
print('=' * 30)
print(deleteAVL(newAvl))
