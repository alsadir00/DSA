# Binary Heap – Short Notes
# 1. What is a Binary Heap? : A Binary Heap is a complete binary tree that satisfies the heap property:
#     Max Heap: Every parent node ≥ its children
#     Min Heap: Every parent node ≤ its children
#     👉 It is commonly implemented using an array, not pointers.

# 2. Why use a Binary Heap? : Binary Heaps are used when we need fast access to the minimum or maximum element.
#     Advantages:
#         Efficient insert and delete
#         Best structure for implementing Priority Queues
#         Uses less memory (array-based)

#     Applications:
#         Priority Queue
#         Heap Sort
#         CPU scheduling
#         Graph algorithms (Dijkstra, Prim)

# 3. Heap Properties
#     Shape Property:
#         Must be a complete binary tree
#         All levels filled except possibly the last (filled left to right)
#         Heap Order Property:
#         Max Heap or Min Heap condition must be maintained

# 5. Array Representation
#     For an element at index i:
#         Parent → (i - 1) / 2
#         Left child → 2i + 1
#         Right child → 2i + 2



class Heap:

    def __init__(self, size):
        self.elements = [None] * (size + 1)
        self.size = 0
        self.maxSize = size + 1
    

def peak(rootNode):
    if not rootNode:
        return "No element is there"
    else:
        return rootNode.elements[1]
        
def Heap_Size(rootNode):
        if  not rootNode:
             return
        else:
             return rootNode.size

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.size+1):
            print(rootNode.elements[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.elements[index] < rootNode.elements[parentIndex]:
            temp = rootNode.elements[index]
            rootNode.elements[index] = rootNode.elements[parentIndex]
            rootNode.elements[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.elements[index] > rootNode.elements[parentIndex]:
            temp = rootNode.elements[index]
            rootNode.elements[index] = rootNode.elements[parentIndex]
            rootNode.elements[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insert(rootNode, value , type):
    if rootNode.size + 1 == rootNode.maxSize:
        return "The binary heap is full"
    rootNode.elements[rootNode.size + 1] = value
    rootNode.size += 1
    heapifyTreeInsert(rootNode, rootNode.size, type)
    print(f"The element {value} is inserted successfully")
    return
    

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.size < leftIndex:
        return
    elif rootNode.size == leftIndex:
        if heapType == "Min":
            if rootNode.elements[index] > rootNode.elements[leftIndex]:
                temp = rootNode.elements[index]
                rootNode.elements[index] = rootNode.elements[leftIndex]
                rootNode.elements[leftIndex] = temp
            return
        else:
            if rootNode.elements[index] < rootNode.elements[leftIndex]:
                temp = rootNode.elements[index]
                rootNode.elements[index] = rootNode.elements[leftIndex]
                rootNode.elements[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.elements[leftIndex] < rootNode.elements[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.elements[index] > rootNode.elements[swapChild]:
                temp = rootNode.elements[index]
                rootNode.elements[index] = rootNode.elements[swapChild]
                rootNode.elements[swapChild] = temp
        else:
            if rootNode.elements[leftIndex] > rootNode.elements[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.elements[index] < rootNode.elements[swapChild]:
                temp = rootNode.elements[index]
                rootNode.elements[index] = rootNode.elements[swapChild]
                rootNode.elements[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

def extract(rootNode, heapType):
    if rootNode.size == 0:
        return
    else:
        extractedNode = rootNode.elements[1]
        rootNode.elements[1] = rootNode.elements[rootNode.size]
        rootNode.elements[rootNode.size] = None
        rootNode.size -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode



heap = Heap(10)
print(levelOrder(heap))
print(Heap_Size(heap))
print(peak(heap))
insert(heap, 2, "Max")
insert(heap, 4, "Max")
insert(heap, 59, "Max")
insert(heap, 40, "Max")
insert(heap, 28, "Max")
insert(heap, 10, "Max")
insert(heap, 11, "Max")
insert(heap, 77, "Max")
insert(heap, 8, "Max")
insert(heap, 100, "Max")

print(levelOrder(heap))
print("=" * 40)
print(Heap_Size(heap))
print("=" * 40)
print(peak(heap))
print("=" * 40)
extract(heap,"Max" )
print(levelOrder(heap))
print("=" * 40)