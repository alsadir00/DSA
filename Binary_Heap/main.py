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
        self.elements = [None] * size + 1
        self.size = size
        self.maxSize = size + 1
    

    def peak(rootNode):
        if not rootNode:
            return "No element is there"
        else:
            return rootNode.elements[1]
        
    
