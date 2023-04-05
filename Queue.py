# http_requests = []
#
# http_requests.insert(0, "link1")
# http_requests.insert(0, "link2")
# http_requests.insert(0, "link3")
#
# print(http_requests)
# print(http_requests.pop())

from collections import deque


class myQueue:

    def __init__(self):
        self.collection = deque()

    def enqueue(self, value):
        self.collection.appendleft(value)

    def dequeue(self):
        return self.collection.pop()

    def peek(self):
        return self.collection[len(self.collection)-1]

    def is_empty(self):
        return len(self.collection) == 0

    def size(self):
        return len(self.collection)


if __name__ == "__main__":
    q = myQueue()

    q.enqueue("link1")
    q.enqueue("link2")
    q.enqueue("link3")
    q.enqueue("link4")
    q.enqueue("link5")

    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())