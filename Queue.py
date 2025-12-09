
# using python list
print("=" * 60)
print("Method One")
print("=" * 60)

class Python_Queue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return True if len(self.elements) == 0 else False
    
    def display(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            for i in self.elements:
                print(i)

    def enqueue(self,value):
        self.elements.append(value)
        print(f"The queue elements after adding the element {value}")
        self.display()
        return

    def dequeue(self):
        if self.isEmpty():
            print("The is not any element in the Queue")
            return
        else:
            print(self.elements.pop(0))
            return

    def peek(self):
        if self.isEmpty():
            print("The is not any element in the Queue")
            return
        else:
            print(self.elements[0])
            return

    def delete(self):
        self.elements = None
        print("the queue is deleted successfully")


Python_Queue_1 = Python_Queue()
Python_Queue_1.enqueue(1)
Python_Queue_1.enqueue(2)
Python_Queue_1.enqueue(3)
Python_Queue_1.enqueue(4)
Python_Queue_1.dequeue()
Python_Queue_1.peek()
Python_Queue_1.delete()



# using python list with limited capacity
print("=" * 60)
print("Method Two")
print("=" * 60)
class Python_Queue_Limited:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1


    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
        


    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1



Python_Queue_Limited_1 = Python_Queue_Limited(5)
Python_Queue_Limited_1.enqueue(1)
Python_Queue_Limited_1.enqueue(2)
Python_Queue_Limited_1.enqueue(3)
Python_Queue_Limited_1.enqueue(4)
Python_Queue_Limited_1.enqueue(5)




# using Deque module
print("=" * 60)
print("Method Three")
print("=" * 60)
from collections import deque


deque_1 = deque(maxlen = 5)
deque_1.append(1)
deque_1.append(2)
deque_1.append(3)
deque_1.append(4)

print(deque_1)
print(deque_1.clear())

# using Queue module
print("=" * 60)
print("Method Four")
print("=" * 60)
import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())
    



 # using multiprocessing.queue as a fifo queue
print("=" * 60)
print("Method Five")
print("=" * 60)       
from multiprocessing import Queue

customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())




# using Linked list
print("=" * 60)
print("Method Six")
print("=" * 60)


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
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None




custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.peek())
print(custQueue)