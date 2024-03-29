class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.start = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        index = self.start
        if self.start >= len(self.sequence):
            self.start = 0
            index = 0
        self.start += 1
        self.counter += 1
        return self.sequence[index]