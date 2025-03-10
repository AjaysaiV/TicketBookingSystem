class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def is_empty(self):
        return self.top is None