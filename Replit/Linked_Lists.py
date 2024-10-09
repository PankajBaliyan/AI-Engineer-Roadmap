# Node class
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion
    def insertAtBegining(self,data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None)

    def insertAtIndex(self,index,data):
        if index < 0 or index > self.getLength():
            raise IndexError("Index out of range")

        if index == 0:
            self.insertAtBegining(data)
            return

        temp = self.head
        count = 0
        while temp:
            if count == index -1:
                temp.next = Node(data,temp.next)
                return
            temp = temp.next
            count += 1

    def insertValues(self,data_list):
        for data in data_list:
            self.insertAtEnd(data)

    # Deletion
    def deleteAtBegining(self):
        if self.head is None:
            raise IndexError("Linkedlist is empty")
        
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            raise IndexError("Linkedlist is empty")
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def deleteAtIndex(self,index):
        if index < 0 or index > self.getLength():
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0
        while temp:
            if count == index - 1:
                if temp.next:
                    temp.next = temp.next.next
                else:
                    raise IndexError("Index out of range")
                return
            temp = temp.next
            count += 1

    def deleteByValue(self,value):
        if self.head is None:
            raise Exception("The Linked List is empty")
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    # Other
    def printList(self):
        if self.head is None :
            print("Linked list is empty")
            return
        
        temp = self.head
        llString = ""
        while temp:
            llString += str(temp.data) + ' -> '
            temp = temp.next
        
        print("Linked List: " + llString[:-4])

    def getLength(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def searchNode(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1

def Main():
    ll = LinkedList()
    # ll.insertAtBegining(10)
    # ll.insertAtBegining(20)
    # ll.insertAtEnd(30)
    ll.insertValues([1,2,3,4,5,6])
    # ll.insertAtIndex(1,100)
    # ll.printList()
    # ll.deleteAtIndex(0)
    # ll.printList()
    # ll.deleteByValue(30)
    # ll.deleteAtBegining()
    # ll.deleteAtEnd()
    ll.printList()
    print(ll.searchNode(2))
    print("Linked List Length is :", ll.getLength())