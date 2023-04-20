def solution():

    def integers():
        integer = 1
        while True:
            yield integer
            integer += 1

    def halves():
        for number in integers():
            yield number / 2

    def take(n, seq):
        result = []
        for number in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)