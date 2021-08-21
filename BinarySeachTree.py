class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None


class BinarySeachTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
            return
        self.check(data, self.root)

    def check(self, data, node):
        if node.data > data:
            if node.left_child:
                self.check(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        elif node.data < data:
            if node.right_child:
                self.check(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def remove(self, data, node):
        if node.data > data:
            self.remove(data, node.left_child)
        elif node.data < data:
            self.remove(data, node.right_child)
        elif node.data == data:
            # Here the real node is already found
            if not node.left_child and not node.right_child:
                if node.parent.left_child == node:
                    node.parent.left_child = None
                elif node.parent.right_child == node:
                    node.parent.right_child = None
            elif node.left_child and not node.right_child:
                node.parent.left_child = node.left_child
            elif not node.left_child and node.right_child:
                node.parent.right_child = node.right_child
            elif node.left_child and node.right_child:
                #DAFUQ tis
                predecessor = self.get_predecessor(node)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove(data, predecessor)

    def traverse(self, node):
        if node.left_child:
            self.traverse(node.left_child)

        print("node data:", node.data)
        if node.right_child:
            self.traverse(node.right_child)

    def get_predecessor(self, node):
        curr = node.left_child
        while curr.right_child:
            curr = curr.right_child
        return curr

    def peek(self):
        return self.root

bst = BinarySeachTree()
bst.insert(4)
bst.insert(5)
bst.insert(2)
bst.insert(1)
bst.insert(3)

bst.traverse(bst.peek())
bst.remove(2, bst.root)
actual = bst.peek()
print('-'*20)
bst.traverse(bst.peek())
while actual:
    print(actual.data)
    actual = actual.left_child

