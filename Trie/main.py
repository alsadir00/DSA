
# 1. What is a Trie? : A Trie (also called a Prefix Tree) is a tree-based data structure used to store strings, especially words, where each node represents a character.
#     Each path from root to a node represents a prefix
#     A special flag marks the end of a word

# 2. Why use a Trie? : Tries are used when we need fast string searching and prefix matching.
#     Advantages:
#         Very fast search, insert, and delete
#         Efficient prefix queries
#         Search time depends on word length, not number of words

#     Applications:
#         Autocomplete and search suggestions
#         Spell checkers
#         Dictionary implementations
#         IP routing
#         Word games

# 3. Trie Properties
#     Root node represents empty string
#     Each edge represents a character
#     Words with common prefixes share nodes
#     Nodes can have multiple children (up to alphabet size)

# 8. Advantages and Disadvantages
#     Advantages:
#         Fast lookup for words
#         Best for prefix-based problems
#         No collisions (unlike hashing)

#     Disadvantages:
#         High memory consumption
#         Not efficient for small datasets
#         Alphabet size affects memory



class Trie_Node:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root = Trie_Node()


    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Trie_Node()
            current = current.children[ch]
        
        current.end_of_string = True
        print('the wor is inserted successfully')

    def search(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                return 'The word can not be here in the Trie' 
            current = current.children[ch]
        
        return 'Found 'if current.end_of_string else 'Not found'


    def starts_with(self, prefix):
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]

        return True

    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            ch = word[index]
            if ch not in node.children:
                return False

            should_delete = _delete(node.children[ch], word, index + 1)

            if should_delete:
                del node.children[ch]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete(self.root, word, 0)


    def deleteString(root, word, index):
        ch = word[index]
        currentNode = root.children.get(ch)
        canThisNodeBeDeleted = False

        if len(currentNode.children) > 1:
            deleteString(currentNode, word, index+1)
            return False
        
        if index == len(word) - 1:
            if len(currentNode.children) >= 1:
                currentNode.endOfString = False
                return False
            else:
                root.children.pop(ch)
                return True
        
        if currentNode.endOfString == True:
            deleteString(currentNode, word, index+1)
            return False

        canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
        if canThisNodeBeDeleted == True:
            root.children.pop(ch)
            return True
        else:
            return False




trie = Trie()
trie.insert("cat")
trie.insert("can")
trie.insert("cap")
print(trie.search("cat"))
print(trie.search("car")) 
print(trie.starts_with("ca")) # True 


