class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.right = None
        self.left = None
        self.value = value
    
    def __str__(self):
        return f" {self.value} "

    def insert(self, value):
        if value == self.value:
            self.left_insert(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left_insert(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right_insert(value)
    
    def left_insert(self, value):
        new_node = Node(value, parent=self)
        new_node.left = self.left
        self.left = new_node
        return new_node

    def right_insert(self, value):
        new_node = Node(value, parent=self)
        new_node.right = self.right
        self.right = new_node
        return new_node

    def walk(self):
        if self.left:
            self.left.walk()
        print(self)
        if self.right:
            self.right.walk()

    def find(self, value):
        if self.value == value:
            return self
        if self.left:
            return self.left.find(value)
        if self.right:
            return self.right.find(value)
        raise Exception("Not Found")

class RBTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        self.root.insert(value)

    def walk(self):
        self.root.walk()
    
    def find(self, value):
        return self.root.find(value)
