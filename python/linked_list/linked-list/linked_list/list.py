class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, next):
        self.head = Node(next,self.head)

    def includes(self, value=None):
        for value in self.head.value:
            if value == self.head:
                return True
            elif value == self.head.next:
                return True
        return False

    def __str__():
        pass
