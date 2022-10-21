class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,val):
        newNode = Node(val)
        self.head = newNode
        self.tail = newNode
        self.length = 1



linkeList = LinkedList(70)
