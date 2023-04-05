class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.start = self.count
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start >= self.end:
            number = self.start
            self.start -= 1
            return number
        raise StopIteration