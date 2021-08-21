class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, data):
        self.length += 1
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return
        self.tail.next = Node(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def peek(self):
        return self.head.data, self.tail.data

    def remove_last(self):
        self.length -= 1
        to_be_removed = self.tail
        self.tail = self.tail.previous
        to_be_removed.previous = None

    def remove_first(self):
        self.length -= 1
        to_be_removed = self.head
        self.head = self.head.next
        to_be_removed.next = None

    def remove_any(self, data):
        curr_node = self.head
        while curr_node and curr_node.data != data:
            curr_node = curr_node.next

        if not curr_node:
            return

        self.length -= 1

        last = curr_node.previous
        next = curr_node.next

        last.next = next
        next.previous = last
        return curr_node

    def get_middle_value(self):
        head_pointer = self.head
        tail_pointer = self.tail

        while head_pointer.data < tail_pointer.data:
            head_pointer = head_pointer.next
            tail_pointer = tail_pointer.previous

        return head_pointer

# important for import