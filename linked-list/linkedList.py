
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
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True 
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        try:
            self.head = self.head.next
            temp.next = None 
            self.length -=1
        except AttributeError:
            print("Something happend ")
        if self.length == 0:
            self.tail= None

        return temp
    
    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        prev_value = self.head
        while temp.next is not None:
            prev_value = temp
            temp = temp.next
        self.tail = prev_value
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
            return None
        return temp.data






           

    def show_list(self):
        temp_var = self.head
        while temp_var is not None:
            print(temp_var.data)
            temp_var = temp_var.next



linkeList = LinkedList()

linkeList.apppend(10)
linkeList.apppend(20)
linkeList.apppend(30)
linkeList.apppend(40)
linkeList.prepend(100)
# print(linkeList.pop())
# print(linkeList.pop())
# print(linkeList.pop())
# print(linkeList.pop())
# print(linkeList.pop())
linkeList.pop_first()
linkeList.pop_first()
linkeList.pop_first()
linkeList.pop_first()
linkeList.pop_first()
linkeList.pop_first()
linkeList.show_list()
