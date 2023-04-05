class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.dictionary_items_list = list(self.dictionary.items())
        self.start = 0
        self.end = len(self.dictionary_items_list)

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            index = self.start
            dict_items = self.dictionary_items_list[index]
            self.start += 1
            return dict_items
        raise StopIteration
