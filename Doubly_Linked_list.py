# this is the file for doubly linked list

print("="*60)
print("doubly linked list")
print("="*60)

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
    

    def create(self, initial_value):
        node = Node(initial_value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        print("Node is created successfully")
        return

    def insert(self, data, location):
        if self.head is None:
            print("please first create the linked list!")
        else:
            new_node = Node(data)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == -1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

    def traverse(self):
        nodes = []
        if self.head is None:
            print("No elements to traverse")
        else:
            temp_node = self.head
            while temp_node:
                nodes.append(str(temp_node.data))
                temp_node = temp_node.next

            print(" -> ".join(nodes))


    def reverse(self):
        nodes = []
        if self.head is None:
            print("No elements to traverse")
        else:
            temp_node = self.tail
            while temp_node:
                nodes.append(str(temp_node.data))
                temp_node = temp_node.prev
            print(" -> ".join(nodes))

    def search(self, value):
        node = self.head
        index = 0
        while node:
            if node.data == value:
                print(f"the value {value} is found at the position {index}")
                return
            index += 1
            node = node.next
        return (f'there is no {value} in the linked list')
    

    def delete(self, location):
        if self.head is None:
            print("No elements to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                cur_node = self.head
                index = 0
                while index < location - 1:
                    cur_node = cur_node.next
                    index += 1
                cur_node.next = cur_node.next.next
                cur_node.next.prev = cur_node
                print("The given node is deleted successfully")
    

    def delete_entire(self):
        if self.head is None:
            print("there is no node in the linked list")
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            print("the DLL has been deleted successfully")
  



Doubly_Linked_List_1 = Doubly_Linked_List()
Doubly_Linked_List_1.create(1)
Doubly_Linked_List_1.insert(2,-1)
Doubly_Linked_List_1.insert(0,0)
Doubly_Linked_List_1.insert(3,-1)
Doubly_Linked_List_1.insert(4,-1)
Doubly_Linked_List_1.insert(6,-1)
Doubly_Linked_List_1.traverse()
Doubly_Linked_List_1.reverse()
Doubly_Linked_List_1.insert(5,5)
Doubly_Linked_List_1.traverse()
Doubly_Linked_List_1.reverse()
Doubly_Linked_List_1.search(3)
Doubly_Linked_List_1.insert(0,0)
Doubly_Linked_List_1.traverse()
Doubly_Linked_List_1.delete(0)
Doubly_Linked_List_1.traverse()
Doubly_Linked_List_1.delete(-1)
Doubly_Linked_List_1.delete(3)
Doubly_Linked_List_1.traverse()


print("="*60)
print("Circular doubly linked list")
print("="*60)


class Circular_Doubly_Linked_List:

    def __init__(self, data = None):
        self.head = None
        self.tail = None

    # creation of CDLL
    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        print("The circular doubly linked list is created successfully")


    # insertion on CDLL
    def insert(self, data, location):

        def locate(location):
            if location == 0:
                return "First"
            elif location == -1:
                return "Last"
            else:
                return (f"At {location}")
            

        if self.head is None:
            print("the circular doubly linked list does not exist")
        else:
            new_node = Node(data)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.prev = self.tail
                new_node.next = self.head
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                new_node.next = temp.next
                new_node.prev = temp
                new_node.next.prev = new_node
                temp.next = new_node
            print(f"The node {data} is successfully inserted to the {locate(location)} position")





    def traverse(self):
        nodes =[]
        if self.head is None:
            print("the circular doubly linked list does not exist")
        else:
            node = self.head
            while node:
                nodes.append(str(node.data))
                if node == self.tail:
                    break
                node = node.next
            print(" -> ".join(nodes))




    def reverse(self):
        nodes =[]
        if self.head is None:
            print("the circular doubly linked list does not exist")
        else:
            node = self.tail
            while node:
                nodes.append(str(node.data))
                if node == self.head:
                    break
                node = node.prev
            print(" -> ".join(nodes))

    def search(self, value):
        node = self.head
        index = 0
        while node:
            if node.data == value:
                print(f"the value {value} is found at the position {index + 1}")
                return
            index += 1
            node = node.next
            if node == self.tail.next:
                return (f'there is no {value} in the linked list')
    

    def delete(self, location):
        if self.head is None:
            print("No elements to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
            else:
                cur_node = self.head
                index = 0
                while index < location - 1:
                    cur_node = cur_node.next
                    index += 1
                cur_node.next = cur_node.next.next
                cur_node.next.prev = cur_node
                print("The given node is deleted successfully")
    
    def delete_entire(self):
        self.head = None
        self.tail.next = None
        self.tail = None

        



        

Circular_Doubly_Linked_List_1 = Circular_Doubly_Linked_List()
Circular_Doubly_Linked_List_1.create(1)
Circular_Doubly_Linked_List_1.insert(2,-1)
Circular_Doubly_Linked_List_1.insert(3,-1)
Circular_Doubly_Linked_List_1.insert(4,-1)
Circular_Doubly_Linked_List_1.insert(5,-1)
Circular_Doubly_Linked_List_1.traverse()
Circular_Doubly_Linked_List_1.reverse()
Circular_Doubly_Linked_List_1.search(3)
Circular_Doubly_Linked_List_1.delete(-1)
Circular_Doubly_Linked_List_1.traverse()
Circular_Doubly_Linked_List_1.delete(1)
Circular_Doubly_Linked_List_1.traverse()
Circular_Doubly_Linked_List_1.delete(0)
Circular_Doubly_Linked_List_1.traverse()




