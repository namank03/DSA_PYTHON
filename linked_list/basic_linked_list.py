class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class LinkedList:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Must be positive")
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def check_capacity_and_inc_size(func):
        def inner(self, *args, **kwargs):
            if self.size >= self.capacity:
                raise IndexError("Capacity Full")
            try:
                func(self, *args, **kwargs)
            except Exception as e:
                print(f'Some Unknown Exception {e} Occured')

            self.size += 1

        return inner

    @check_capacity_and_inc_size
    def prepend(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

    @check_capacity_and_inc_size
    def append(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            self.tail = node
            temp.next = node

    @check_capacity_and_inc_size
    def insert(self, data, pos):
        if pos > self.size:
            raise ValueError(
                f"Can't remove element from this position, position must be less than current size = {self.size}",
            )
        node = Node(data)
        current = self.head
        for _ in range(pos - 1):
            current = current.next

        node.next = current.next
        current.next = node

    def remove(self, pos):
        if pos > self.size:
            raise ValueError(
                f"Can't remove element from this position, position must be less than current size = {self.size}",
            )

        previous = self.head

        for _ in range(pos - 1):
            previous = previous.next
        current = previous.next

        previous.next = current.next
        current.next = None

        self.size -= 1

    def __str__(self):
        return self.head.__str__()


linked_list = LinkedList(10)
linked_list.prepend(9)
linked_list.prepend(0)
print(linked_list.size)
linked_list.prepend(3)
linked_list.prepend(10)
print(linked_list.size)
linked_list.append(90)
linked_list.append(100)
linked_list.insert(4, 4)
print(linked_list.size)
print(linked_list)
linked_list.remove(4)
print(linked_list)
