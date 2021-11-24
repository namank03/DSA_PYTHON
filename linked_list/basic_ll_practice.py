

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_start(self, data):
        node = Node(data)

        if self.head is None:
            self.head, self.tail = node, node
        else:
            node.next = self.head
            self.head = node
        return self.head

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next

    def add_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node
            self.tail = node
        return self.head

    def __str__(self):
        return "->".join((str(i)) for i in self)


ll = LinkedList()

ll.add_start(2)
ll.add_end(20)
ll.add_end(10)
ll.add_end(50)
ll.add_end(60)
ll.add_end(4)

print(ll)
