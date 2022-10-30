class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, val=None):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Add new item the list
    def add(self, value):
        new_node = Node(value)
        if self.length == 0 or self.head.data is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # print linklist
    def display(self):
        temp_var = self.head
        while temp_var is not None:
            print(temp_var.data)
            temp_var = temp_var.next


ll = LinkedList()
ll.add(120)
ll.add(150)
ll.add(170)
ll.display()
