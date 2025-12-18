class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size
    
    def insert(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"
        self.custom_list[self.last_used_index+1] = value
        self.last_used_index += 1
        print(f"The value {value} has been successfully inserted")
        return

    def search(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                print(f"Success The Node {node_value} is inside the tree at index {i}")
                return
        print("Not found")
        return
    
    def preOrder(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.preOrder(index*2)
        self.preOrder(index*2 + 1)

    def inOrder(self, index):
        if index > self.last_used_index:
            return
        self.inOrder(index*2)
        print(self.custom_list[index])
        self.inOrder(index*2+1)
    
    def postOrder(self, index):
        if index > self.last_used_index:
            return
        self.postOrder(index*2)
        self.postOrder(index*2+1)
        print(self.custom_list[index])
    
    def levelOrder(self, index):
        for i in range(index, self.last_used_index+1):
            print(self.custom_list[i])
    
    def delete(self, value):
        if self.last_used_index == 0:
            return "There is not any node to delete"
        for i in range(1, self.last_used_index+1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "The node has been successfully deleted"
    
    def deleteBT(self):
       self.custom_list = None
       return "The BT has been successfully deleted"

    
 

newBT = BinaryTree(10)
newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")
newBT.insert("Cola")
newBT.insert("fanta")
newBT.insert("coca")
newBT.insert("pepsi")



newBT.levelOrder(1)