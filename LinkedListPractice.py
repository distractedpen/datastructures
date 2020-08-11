class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

head = None
current = None

def insertFirst(data): #O(1)
    global head
    node = Node(data)
    node.next = head
    head = node

def insertAfter(node_data, data): #O(n)
    new_node = Node(data)
    prev = searchList(node_data)
    new_node.next = prev.next
    prev.next = new_node

def deleteFirst(): #O(1)
    global head
    removed_link = head
    head = head.next
    return removed_link


def printList(): #O(n)
    global head
    current = head
    print("\n[ ", end="");
    while(current != None):
        print("({0})".format(current.data), end=" ")
        current = current.next
    print(" ]\n")

def searchList(data): #O(n)
    #using a linear search
    global head
    current = head
    while(current.data != data):
        if (current.next == None):
            return None
        else:
            current = current.next
    return current

def main():
    insertFirst(3)
    insertFirst(4)
    insertFirst(5)
    printList()
    printList()
    insertFirst(9)
    print(bool(searchList(3)))
    printList()
    insertAfter(5, 6)
    printList()

if __name__ == "__main__":
    main()
