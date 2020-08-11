class Stack:

    def __init__(self, max_size):
        self.s = []
        self.MAXSIZE = max_size
        self.top = -1

    def isEmpty(self):
        return self.s == []

    def push(self, data):
        self.s.append(data)
        return

    def pop(self):
        return self.s.pop()

    def peek():
        return self.s[len(self.s)-1]

    def size(self):
        return len(self.s)

