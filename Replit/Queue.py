from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self,value):
        self.container.appendleft(value)

    def dequeue(self):
        self.container.pop()

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
        

def Main(): 
    print("Queue Data Structure")
    q = Queue()
    q.enqueue(5)
    q.enqueue(2)
    q.enqueue(1)
    print(q.container)
    q.dequeue()
    print(q.container)
    print(q.isEmpty())
    print(q.size())