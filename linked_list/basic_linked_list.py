class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class LinkedList:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def prepend(self, data):
        if self.size >= self.capacity:
            return "Exceeded capacity"
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

        self.size += 1

    def __str__(self):
        return self.head.__str__()


linked_list = LinkedList(4)
linked_list.prepend(9)
linked_list.prepend(0)
linked_list.prepend(3)
linked_list.prepend(10)
print(linked_list)
