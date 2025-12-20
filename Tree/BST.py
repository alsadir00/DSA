#  operations here are 
    # creation
    # insertion
    # deletion of a node 
    # search for the value
    # traverse all the value
    # deletion of the tree
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

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTNode(value)
        else:
            insert(rootNode.left, value)
    else:
        if rootNode.right is None:
            rootNode.right = BSTNode(value)
        else:
            insert(rootNode.right, value)
    return "The node of value has been successfully inserted"

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


def minValue(bstNode):
    current = bstNode
    while (current.left is not None):
        current = current.left
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        
        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        
        temp = minValue(rootNode.right)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.right, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "The BST has been successfully deleted"



newBST = BSTNode(None)
insert(newBST, 70)
insert(newBST,50)
insert(newBST,90)
insert(newBST, 30)
insert(newBST,60)
insert(newBST,80)
print(insert(newBST,100))
insert(newBST,20)
insert(newBST,40)
insert(newBST, 25)
insert(newBST, 18)
insert(newBST, 110)



print("Level Order Traversal")
levelOrder(newBST)
print("="* 50)

print("Pre Order Traversal")
preOrder(newBST)
print("="* 50)

print("In Order Traversal")
inOrder(newBST)
print("="* 50)

print("Post Order Traversal")
postOrder(newBST)
print("="* 50)



print("Search for the value")
search(newBST, 50)
print("="* 50)

print("Minimum value of the tree")
print(minValue(newBST).data)
print("="* 50)