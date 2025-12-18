# types of binary tree :
#     1. full binary tree when the node has either 0 or 2 childrens
#     2. perfect Binary tree : when tree is binary and the level of the leafs are the same 
#     3. complete binary tree : all the un complete level lays on the left side of hte tree
#     4. balanced tree : when all the leafs are located to the same distance fro the root


#  binary tree maybe represented into two ways using python list and linked list method
# In linked list method, each nodes has three components. right, left and data. when the right and the left represents the edges or the address of the child. in essence when there is no child it points to null
# in second method using python list, we left the 0 index for calculation simplification matter  and we assign the the x value to point to the root or the index of the root then leftchild = cell[2x] and right child = cell[2x+1]
# left child = cell[2x] and right child = cell[2x+1]



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
    





class Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None





New_Tree = Tree("Root")

left_1= Tree("First Left")
right_1 = Tree("First Right")
New_Tree.left = left_1
New_Tree.right = right_1

left_2 = Tree("Second Left Left")
right_2 = Tree("Second Left Right")
left_1.left = left_2
left_1.right = right_2

left_3 = Tree("Second Right Left")
right_3 = Tree("Second Right Right")
right_1.left = left_3
right_1.right = right_3

left_4 = Tree("Ma Left")
right_4 = Tree("Ma right")
left_5 = Tree("Ma m Left")
right_5 = Tree("Ma m right")

left_6 = Tree("mariana 1 Left")
right_6 = Tree("mariana 1 right")
left_7 = Tree("mariana 2 Left")
right_7 = Tree("mariana 2 right")

left_2.left = left_4
left_2.right = right_4

right_2.right = right_5

left_3.right = right_6

right_3.right = right_7
right_3.left = left_7



# time and space complexities are o(n) for both space and time
#  traversal  in tree is depth first [ pre order, in order, post order] and breadth first [level order traversal]
def preOrder(tree_root):  # root -> left -> right
    if not tree_root:
        return "There is no root node here"
    else:
        print(tree_root.data)
        preOrder(tree_root.left)
        preOrder(tree_root.right)


def inOrder(tree_root): # left -> root -> right
    if not tree_root:
        return "There is no root node here"
    inOrder(tree_root.left)
    print(tree_root.data)
    inOrder(tree_root.right)


def postOrder(tree_root): # root -> left -> right
    if not tree_root:
        return "There is no root node here"
    postOrder(tree_root.left)
    postOrder(tree_root.right)
    print(tree_root.data)
    

def levelOrder(tree_root):
    if not tree_root:
        return "There is no root node here"
    else:
        customQueue = Queue()
        customQueue.enqueue(tree_root)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if(root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)

def search(tree_root, value):
    if not (tree_root):
        return "There is no root node here"
    else:
        customQueue = Queue()
        customQueue.enqueue(tree_root)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == value:
                print("Found")
                return 
            if(root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
        return "Not Found in The Tree"
 

def insert(tree_root, value):
    if not (tree_root):
        tree_root = value 
    else:
        customQueue = Queue()
        customQueue.enqueue(tree_root)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if(root.value.left is not None):
                customQueue.enqueue(root.value.left)
            else:
                root.value.left = value
                print("Success on the left")
                return 
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
            else:
                root.value.right = value
                print("Success on the right")
                return 
            


def getDeepest(tree_root):
    if not tree_root:
        return "There is no root node here"
    else:
        customQueue = Queue()
        customQueue.enqueue(tree_root)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if(root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
        deepest = root.value
        return deepest

def deleteDeepest(tree_root,deepest):
    if not tree_root:
        return "There is no root node here"
    else:
        customQueue = Queue()
        customQueue.enqueue(tree_root)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is deepest:
                root.value = None
                return
            if root.value.right:
                if root.value.right is deepest:
                    root.value = None
                    return
                else:
                    customQueue.enqueue(root.value.right)
            if root.value.left:
                if root.value.left is deepest:
                    root.value = None
                    return
                else:
                    customQueue.enqueue(root.value.left)


def deleteNode(tree_root, value):
    if not tree_root:
        return "There is no root node here"
    else:
        customQueue = Queue()
        customQueue.enqueue(tree_root)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == value:
                new_node = getDeepest(tree_root)
                root.value.data = new_node.data
                deleteDeepest(tree_root, new_node)
                return "Deleted Successfully"
            
            if(root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
        return "Deletion Failed"


        
def delete_entire(tree_root):
    tree_root.data = None
    tree_root.right = None
    tree_root.left = None




print("="*50)
print("PreOrder Traversal")
print("="*50)
preOrder(New_Tree)


print("="*50)
print("InOrder Traversal")
print("="*50)
inOrder(New_Tree)

print("="*50)
print("PostOrder Traversal")
print("="*50)
postOrder(New_Tree)

print("="*50)
print("Level Order Traversal")
print("="*50)
levelOrder(New_Tree)

print("="*50)
print("Find, Node")
search(New_Tree, 'mariana 2 right')
print("="*50)


print("="*50)
print("Insert, Node")
new_node = Tree("Mariana 3")
insert(New_Tree, new_node)
print("="*50)

print("="*50)
print("Get Deepest Node")
deepest = getDeepest(New_Tree)
print(f"the deepest node in the tree is \"{deepest.data}\"")
print("="*50)



