from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()

    # Push function will insert value at end
    def push(self, value):
        self.container.append(value)

    # Pop function will delete last inserted value
    def pop(self):
        self.container.pop()

    # Peek function will return the top element of stack
    def peek(self):
        return self.container[-1]

    # IsEmpty function will check is stack is empty or not
    def isEmpty(self):
        return len(self.container) == 0
    
    # Size function will return size of stack
    def size(self):
        return len(self.container)

    # Print function will print the whole stack
    def print(self):
        print(self.container)

def Main():

    # Direct Way
    # stack.append(30)
    # stack.append(20)
    # stack.append(10)
    # stack.pop()
    # print(stack)

    # Using class
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.pop()
    print(s.peek())
    print(s.isEmpty())
    print(s.size())
    s.print()