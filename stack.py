# stack = []
#
# stack.append("link1")
# stack.append("link2")
# stack.append("link3")
# stack.append("link4")
# stack.append("link5")
#
# print("before pop : ", str(stack))
# print(stack.pop())
# print("after pop : ", str(stack))

# in here we are using list but the problem is ,
# when it large the size it add 2fold current space so it can be huge memory allocation

# Now we are using deque which is created by using linked list

# from collections import deque
# stack = deque()
# #print(dir(stack))
# print("-------------------------")
# stack.append("link1")
# stack.append("link2")
# stack.append("link3")
# stack.append("link4")
# stack.append("link5")
# print(stack)

from  collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == "__main__":
    stack = Stack()

    print("-------------------------")
    stack.push("link1")
    stack.push("link2")
    stack.push("link3")
    stack.push("link4")
    stack.push("link5")
    print(stack.pop())