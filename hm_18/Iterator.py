class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value

lst = [1, 2, 3, 4, 5]
for item in ReverseListIterator(lst):
    print(item)

# 2

class EvenNumbersIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

for even in EvenNumbersIterator(10):
    print(even)