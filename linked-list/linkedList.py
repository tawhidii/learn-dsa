
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,value):
        newNode = Node(value)
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
        return temp
    
    # Get Node 
    def get(self,index):
        if index < 0 or index >= self.length:
            return "index is greater or less than LL"
        temp_head = self.head
        for _ in range(index):
            temp_head = temp_head.next
        return temp_head

    # Set value
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.data = value
            return True

        return False


    def show_list(self):
        temp_var = self.head
        while temp_var is not None:
            print(temp_var.data)
            temp_var = temp_var.next



linkeList = LinkedList(44)
linkeList.apppend(10)
linkeList.apppend(20)
linkeList.apppend(30)
linkeList.apppend(40)
linkeList.apppend(100)

# print(linkeList.length)
linkeList.set_value(2,1000)
# a = linkeList.get(2)
# print(a.data)
linkeList.set_value(4,500)

# linkeList.show_list()
# print(linkeList.get(2).data)
# print(linkeList.pop())
# print(linkeList.pop())
# print(linkeList.pop())
# print(linkeList.pop())
# print(linkeList.pop())
# linkeList.pop_first()
# linkeList.pop_first()
# linkeList.pop_first()
# linkeList.pop_first()
# linkeList.pop_first()
# linkeList.pop_first()
linkeList.show_list()

