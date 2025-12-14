#  why tree ?
#  quick and easier access for the data inside the tree


class Node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = []


    def __str__(self, level = 0):
        ret = ' ' * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild( self, TreeNode):
        self.children.append(TreeNode)


tree = Node("Drinks",[])
cold = Node("Cold", [])
hot = Node("Hot", [])
tea = Node("Tea", [])
coffee = Node("coffee", [])
fanta = Node("Fanta", [])
cola = Node("Cola", [])


cold.addChild(fanta)
cold.addChild(cola)
tree.addChild(cold)
tree.addChild(hot)
print(tree)

