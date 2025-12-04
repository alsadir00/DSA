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
    

    


singly_linked_list_1 = Singly_Linked_List()
singly_linked_list_1.insert(10, -1)
singly_linked_list_1.insert(20, -1)
singly_linked_list_1.insert(30, -1)
singly_linked_list_1.insert(94,0)
singly_linked_list_1.insert(40, -1)
singly_linked_list_1.insert(60, 2)
singly_linked_list_1.insert(70, 3)

singly_linked_list_1.display()
print(singly_linked_list_1.search_value(20))
print(singly_linked_list_1.search_value(100))
singly_linked_list_1.insert(50, 2)
singly_linked_list_1.traversal()
singly_linked_list_1.delete_node(0)
singly_linked_list_1.traversal()
singly_linked_list_1.delete_node(-1)
singly_linked_list_1.traversal()
Singly_Linked_List_2 = Singly_Linked_List()
Singly_Linked_List_2.traversal()
singly_linked_list_1.traversal()