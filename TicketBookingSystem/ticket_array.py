class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.count = 0

    def append(self, item):
        if self.count < self.size:
            self.data[self.count] = item
            self.count += 1

    def remove(self, item):
        for i in range(self.count):
            if self.data[i] == item:
                self.data[i] = None
                self.count -= 1
                break

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return self.count