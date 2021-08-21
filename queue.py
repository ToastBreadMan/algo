from DoublyLinkedList import DoublyLinkedList


class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def pop(self):
        if not self.queue:
            return
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val

    def peek(self):
        if self.queue:
            return self.queue[0]


class DllQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def insert(self, data):
        self.queue.insert(data)

    def pop(self):
        if not self.queue.length:
            return
        val = self.queue.peek()[0]
        self.queue.remove_first()
        return val

    def peek(self):
        if self.queue.length:
            return self.queue.peek()