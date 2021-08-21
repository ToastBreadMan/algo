class Stack:
    def __init__(self):
        self.stack = []
        self.max_value = 0

    def push(self, data):
        self.stack.append(data)

        if data > self.max_value:
            self.max_value = data

    def pop(self):
        if not self.stack:
            return
        last_elem = self.stack[-1]
        del self.stack[-1]
        return last_elem

    def peek(self):
        return self.stack[-1]

    def stack_length(self):
        return len(self.stack)

    def get_max_value(self):
        return self.max_value

stack = Stack()

stack.push(1)
stack.pop()
stack.pop()

print(stack.get_max_value())