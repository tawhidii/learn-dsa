

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,val=None):
        newNode = Node(val)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def apppend(self,value):
        newNode = Node(value)
        if self.length == 0 or self.head.data is None:
            self.head = newNode
            self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1


    def show_list(self):
        temp_var = self.head
        while temp_var is not None:
            print(temp_var.data)
            temp_var = temp_var.next



linkeList = LinkedList()
linkeList.apppend(170)

linkeList.show_list()