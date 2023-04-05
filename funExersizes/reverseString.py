from  collections import deque
stack = deque()

string = "SriLanka"
reversedString = ''

for i in string:
    stack.append(i)
print(stack)

while len(stack)>0:
    reversedString += stack.pop()

print(reversedString)