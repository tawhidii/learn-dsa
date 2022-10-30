class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def getValue(self, data):
        if self.head is None:
            return "LinkedList is empty"
        tmp = self.head
        while tmp:
            if tmp.data == data:
                return "data is found"+str(tmp.data)
            tmp = tmp.next
        return "data is not found "

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            return

        tmp = self.head

        while tmp.next:
            tmp = tmp.next

        tmp.next = Node(data, None)
        self.tail = tmp.next
        return

    def show(self):
        if self.head is None:
            return "LinkedList is empty"
        joinData = ""
        tmp = self.head

        while tmp:
            joinData += str(tmp.data)+"------->"
            tmp = tmp.next
        return joinData


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print(ll.getValue(333))
