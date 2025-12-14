#  SINGLY LINKED LIST IMPLEMENTATION IN PYTHON


class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, data, location): # time complexity = o(n) space is o(1)
        new_node = Node(data) # empty node created

        # here we have three cases to handle :- at the beginning, at the end, at any given
        if self.head is None: # empty linked list
                self.head = new_node
                self.tail = new_node
        else:
            if location == 0: # insert at beginning
                new_node.next = self.head # first make the new node point to the current head
                self.head = new_node
            elif location == -1: # insert at end
                self.tail.next = new_node # first make the current tail node point to the new node
                self.tail = new_node # make the given new node to the be tail
            else: # insert at given location
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def display(self): #time and space(since there is nodes list) complexity is o(n)
        nodes = []
        temp_node = self.head
        while temp_node:
            nodes.append(str(temp_node.data))
            temp_node = temp_node.next
        print(" -> ".join(nodes))

    def traversal(self):   #time and space(since there is nodes list) complexity is o(n)
        nodes = []
        if self.head is None:
            print("the linked list is none!")
        else:
            node = self.head
            while node is not None:
                nodes.append(str(node.data))
                node = node.next
            print(" -> ".join(nodes))
    
    def search_value(self, value): # time complexity is o(n) space is o(1)
        if self.head is None:
            return "the linked list is empty"
        else:
            node = self.head
            while node is not None:
                if node.data == value:
                    return f"{value} found in the linked list"
                node = node.next
            return f"{value} not found in the linked list"
    
    def delete_node(self, location): # time complexity is o(n) space is o(1)
        if self.head is None:
            print("the linked list is empty") # nothing to delete
        else:
            if location == 0:
                if self.head == self.tail:  # delete first node when there is only one node
                    self.head = None
                    self.tail = None
                else: # delete first node when there are multiple nodes
                    self.head = self.head.next
            elif location == -1: # delete last node
                temp_node = self.head
                while temp_node.next.next:
                    temp_node = temp_node.next
                temp_node.next = None
                self.tail = temp_node
            else: # delete at given location
                index = 0
                temp_node = self.head
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next.next
                temp_node.next = next_node

    def delete_entire_list(self): # both time and space complexity are of o(1)
        if self.head is None:
            return "the single linked list is empty"
        else:
            self.head = None
            self.tail = None
    

    


singly_linked_list_1 = Singly_Linked_List()
singly_linked_list_1.insert(10, -1)
singly_linked_list_1.insert(20, -1)
singly_linked_list_1.insert(30, -1)
singly_linked_list_1.insert(94,0)
singly_linked_list_1.insert(40, -1)
singly_linked_list_1.insert(60, 2)
singly_linked_list_1.insert(70, 3)

singly_linked_list_1.display() # shows 94 -> 10 -> 60 -> 70 -> 20 -> 30 -> 40
print(singly_linked_list_1.search_value(20)) # 20 found in the linked list
print(singly_linked_list_1.search_value(100)) # 100 not found in the linked list
singly_linked_list_1.insert(50, 2)
singly_linked_list_1.traversal() # 94 -> 10 -> 50 -> 60 -> 70 -> 20 -> 30 -> 40
singly_linked_list_1.delete_node(0)
singly_linked_list_1.traversal()# 10 -> 50 -> 60 -> 70 -> 20 -> 30 -> 40
singly_linked_list_1.delete_node(-1)
singly_linked_list_1.traversal() # 10 -> 50 -> 60 -> 70 -> 20 -> 30
Singly_Linked_List_2 = Singly_Linked_List()
Singly_Linked_List_2.traversal() # the linked list is none!
singly_linked_list_1.traversal() # 10 -> 50 -> 60 -> 70 -> 20 -> 30


print("====================================================")

class Circular_Singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, data):
        node = Node(data= data)
        node.next = node
        self.head = node
        self.tail = node
        print("Node is created successfully")
        return


    def insert(self, data, location):
        if self.head is None:
            print("There is no Node that references circular singly linked")
            return
        else:
            node = Node(data)
            if location == 0:
                node.net = self.head
                self.head = node
                self.tail.next = node
            elif location == -1:
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node              
            else:
                temp_node = self.head
                index = 0 
                while index < location-1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = node
                node.next = next_node

    

    def traverse(self):
        nodes = []
        if self.head is None:
            print("The circular singly linked is empty")
            return
        else:
            node = self.head
            while node:
                nodes.append(str(node.data))
                node = node.next
                if node == self.tail.next:
                    break
        print(" -> ".join(nodes))


    def search(self, value):
        if self.head is None:
            print("There is no node reference ")
        else:
            i = 0
            node = self.head
            while node:
                if node.data == value:
                    print(f'the value {value} is found on the {i+1}th position')
                    return 
                node = node.next
                i += 1
                if node == self.tail.next:
                    print(f"the value {value} doesn't fo und on the linked list")
                    return


    def delete(self, location):
        if self.head is None:
            print("The Linked List is Empty")
            return
        else:
            if location == 0:
                if self.head == self.tail.next:
                    self.tail = None
                    self.head = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail.next:
                    self.tail = None
                    self.head = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                temp_node = self.head
                i = 0 
                while i < location - 1:
                    temp_node  = temp_node.next
                    i += 1
                next_node =  temp_node.next
                temp_node.next = next_node.next
    

    def delete_entire(self):
        self.head = None
        self.tail.next = None
        self.tail = None
         


                    

                    
                


Circular_Singly_linked_list_1 = Circular_Singly_linked_list()
Circular_Singly_linked_list_1.create(1)
Circular_Singly_linked_list_1.insert(2,-1)
Circular_Singly_linked_list_1.insert(3,-1)
Circular_Singly_linked_list_1.insert(4,-1)
Circular_Singly_linked_list_1.insert(5,-1)
Circular_Singly_linked_list_1.insert(6,-1)
Circular_Singly_linked_list_1.insert(7,-1)
Circular_Singly_linked_list_1.insert(8,-1)
Circular_Singly_linked_list_1.traverse()
Circular_Singly_linked_list_1.search(6)
Circular_Singly_linked_list_1.delete(2)
Circular_Singly_linked_list_1.traverse()


