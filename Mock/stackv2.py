class StackV2:

    def __init__(self, c):
        self.data = [None] * c
        self.map = [i for i in range(c)]
        self.next = c - 1
        self.capacity = c

    def push(self, o):
        if self.next == -1:
            return -1
        key = self.map[self.next]
        self.next -= 1
        self.data[key] = o
        return key

    def get(self, k):
        if k <= 0 or k >= self.capacity:
            return -1
        if self.data[k] == None:
            return -2
        return self.data[k]

    def free(self, k):
        if k <= 0 or k >= self.capacity:
            return -1
        if self.data[k] == None:
            return -2
        self.data[k] = None
        self.next += 1
        self.map[self.next] = k
        return 0

    def __repr__(self):
        for item in self.data:
            return str(self.data)
