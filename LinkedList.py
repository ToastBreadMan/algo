class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = Node(data)
        return

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        return self.head

    def remove_first(self):
        to_be_removed = self.head
        self.head = self.head.next
        to_be_removed.next = None
        del to_be_removed

    def remove_last(self):
        curr_node = self.head
        while curr_node.next.next:
            curr_node = curr_node.next
        curr_node.next = None

    def find_middle(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow.data

    def reverse(self):
        last = None
        curr = self.head
        next = self.head.next
        while next:
            curr.next = last
            last = curr
            curr = next
            next = next.next
        curr.next = last
        self.head = curr

    def all(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next

ll = LinkedList()
for i in range(10):
    ll.insert(i)

print(ll.find_middle())
ll.all()
print('-'*20)
ll.reverse()
ll.all()

print(ll.find_middle())
