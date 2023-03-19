class reverse_iter:
    def __init__(self, iterable: list):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.iterable):
            raise StopIteration

        self.index -= 1
        return self.iterable[self.index + 1]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
