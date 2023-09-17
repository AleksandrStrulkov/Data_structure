class QueueRightToleft:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


class QueueLeftToRight:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = QueueRightToleft()
    q.enqueue(1)
    print(q.items)
    q.enqueue(2)
    print(q.items)
    q.enqueue(3)
    print(q.items)
    q.enqueue(4)
    print(q.items)
    q.dequeue()
    print(q.items)
    q.dequeue()
    q = QueueLeftToRight()
    q.enqueue(1)
    print(q.items)
    q.enqueue(2)
    print(q.items)
    q.enqueue(3)
    print(q.items)
    q.enqueue(4)
    print(q.items)
    q.dequeue()
    print(q.items)
    q.dequeue()
    print(q.items)