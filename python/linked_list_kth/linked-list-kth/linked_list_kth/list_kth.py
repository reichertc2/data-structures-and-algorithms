class Node:
    def __init__(self, value, next=0):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = None

    def insert(self, next):
        self.head = Node(next,self.head )
