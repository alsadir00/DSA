# Questions: 1. is there any collection in python for stack implementation? like that makes the usage of the stack for us fast and efficient?

# METHOD - 1 
# there is no built-in stack in python but we can use list as stack and this method is for dynamic stack implementation with no length limit.

print("=" * 60)
print("Method One")
print("=" * 60)
class Classic_Stack:
    def __init__(self):
        self.items = []
    

    def is_empty(self):  # O(1) complexity for both time and space 
        return self.items == []
    
    
    def push(self, item): # O(1)/amortized complexity for both time and space
        self.items.append(item)
        return "Item pushed successfully"

    def pop(self): # O(1) complexity for both time and space
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    
    def peek(self): # O(1) complexity for both time and space
        if self.is_empty():
            return "Stack is empty"
        return self.items[len(self.items)-1]
    

    def size(self): # O(1) complexity for both time and space
        return len(self.items)
    

    def display(self): # O(n) complexity for time and O(1) for space
        print(self.items) 


    def delete(self): # O(1) complexity for both time and space
        self.items = None  
    

Classic_Stack_1 = Classic_Stack()
Classic_Stack_1.push(1)
Classic_Stack_1.push(2) 
Classic_Stack_1.push(3)
Classic_Stack_1.display()
Classic_Stack_1.pop()
Classic_Stack_1.display()
print(Classic_Stack_1.peek())


print("=" * 60)
print("Method Two")
print("=" * 60)
# METHOD - 2  using python list with limited size

class limited_stack:
    def __init__(self,max_size):
        self.items = []
        self.max_size = max_size

    def is_empty(self): # O(1) complexity for both time and space
        return self.items == []
    
    def is_full(self): # O(1) complexity for both time and space
        return len(self.items) == self.max_size
    
    def push(self, item): # O(1)/ amortized  complexity for both time and  space
        if self.is_full():
            return "Stack is full"
        self.items.append(item)
        return "Item pushed successfully"

    def pop(self): # O(1) complexity for both time and space
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self): # O(1) complexity for both time and space
        if self.is_empty():
            return "Stack is empty"
        return self.items[len(self.items)-1]
    
    def size(self): # O(1) complexity for both time and space
        return len(self.items)
    
    def display(self): # O(n) complexity for time and O(1) for space
        print(self.items)   
    
    def delete(self): # O(1) complexity for both time and space
        self.items = None


limited_stack_1 = limited_stack(3)
print(limited_stack_1.push(10) )
print(limited_stack_1.push(20))
print(limited_stack_1.push(30))
print(limited_stack_1.display())
print(limited_stack_1.push(40))
print(limited_stack_1.pop())
print(limited_stack_1.display())
print(limited_stack_1.peek())


print("=" * 60)
print("Method Three")
print("=" * 60)
# METHOD - 3 using linked list for stack implementation
class Node:
    def __init__(self, value = None):
        self.next = None
        self.value = value


class Linked_list:
    def __init__(self):
        self.head = None


class Linked_List_stack:
    def __init__(self):
        self.Linked_list = Linked_list()

    
    def isEmpty(self):
        return True if self.Linked_list.head == None else False

    def display(self):
        if self.isEmpty():
            print("There is no element in the stack")
            return
        else:
            elements = []
            cur = self.Linked_list.head
            while cur:
                elements.append(str(cur.value)) 
                cur = cur.next
            for i in elements:
                print(i)
            return
    
    def push(self,  value):
        new_node = Node(value)
        new_node.next = self.Linked_list.head
        self.Linked_list.head = new_node
        print(f"Elements in the stack after adding value {value} is:")
        self.display()
        return

    def pop(self):
        if self.isEmpty():
            print("There is no element in the stack")
            return
        else:
            value = self.Linked_list.head.value
            self.Linked_list.head = self.Linked_list.head.next
            print(f"Elements in the stack after popping value {value} is:")
            self.display()
            return

    def peak(self):
        if self.isEmpty():
            print("There is no element in the stack")
            return
        else:
            value = self.Linked_list.head.value
            print(f"The first element in the stack is: {value}")
            return
    
    def size(self):
            elements = []
            cur = self.Linked_list.head
            while cur:
                elements.append(str(cur.value)) 
                cur = cur.next
            print(f"The size of the stack is: {len(elements)}")

    def delete(self):
        self.Linked_list.head = None
        print("The stack is become empty")
        return


    





Linked_List_stack_1 = Linked_List_stack()
print(Linked_List_stack_1.isEmpty())
Linked_List_stack_1.push(1)
Linked_List_stack_1.push(2)
Linked_List_stack_1.push(3)
Linked_List_stack_1.pop()
Linked_List_stack_1.push(3)
Linked_List_stack_1.push(4)
Linked_List_stack_1.push(5)
Linked_List_stack_1.peak()
Linked_List_stack_1.size()


