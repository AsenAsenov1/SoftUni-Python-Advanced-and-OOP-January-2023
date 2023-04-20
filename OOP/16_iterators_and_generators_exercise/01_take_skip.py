class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter <= self.count:
            index = self.start
            self.start += self.step
            self.counter += 1
            return index
        raise StopIteration
