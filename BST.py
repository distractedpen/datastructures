import random

class Node():

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree():
#Binary Tree algorithms
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if new_node.data <= current.data:
                    if current.left_child == None:
                        current.left_child = new_node
                        return
                    else:
                        current = current.left_child
                else:
                    if current.right_child == None:
                        current.right_child = new_node
                        return
                    else:
                        current = current.right_child

    def printTree(self):
        def printSubTree(node):
            if node.left_child != None:
                temp = printSubTree(node.left_child) + " {0}".format(node.data)
                if node.right_child != None:
                    return temp + " " + printSubTree(node.right_child)
                else:
                    return temp
            elif node.right_child != None:
                return "{0} ".format(node.data) + printSubTree(node.right_child)
            else:
                return "{0}".format(node.data)
                
        return print(printSubTree(self.root))
                
        
    def minValue(self):
        def traverseLeft(node):
            if node.left_child != None:
                return traverseLeft(node.left_child)
            else:
                return node.data
        v = traverseLeft(self.root)
        return v

    def maxValue(self):
        def traverseRight(node):
            if node.right_child != None:
                return traverseRight(node.right_child)
            else:
                return node.data
        v = traverseRight(self.root)
        return v

#test code
def main():
    bst = BinarySearchTree()
    a = [7, 53, 17, 71, 63, 67, 41, 41,
         34, 79, 83, 95, 21, 49, 53, 73, 84, 22, 7, 99]
    for n in a:
        bst.insert(n)
##    for i in range(20):
##        r = random.randint(0, 100)
##        print(r, end=" ")
##        bst.insert(r)
##    print("\n")
    bst.printTree()
    

if __name__ == "__main__":
    main()
            
        
        
        
        
        
    
    
        
