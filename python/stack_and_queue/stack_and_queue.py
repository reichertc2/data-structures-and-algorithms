class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self, value):
        if self.top != None:
            # print('push value:', value.value)
            old_top = self.top
            self.top = value
            value.next = old_top
        if self.top == None:
            # print('push value:', value.value)
            self.top = value
            value.next = None

    def pop(self):
        if self.top != None:
            old_top = self.top
            self.top = old_top.next
            return old_top.value
        if self.top == None:
            return Exception

    def peek(self):
        if self.top == None:
            return Exception
        return self.top.value

    def is_empty(self):
        if self.top != None:
            return False
        return True


class Queue:
    def __init__(self, front = None):
        self.front = front
        self.rear = None

    def enqueue(self, value = None):

        node = Node(value)

        if self.rear:
            self.rear.next = node

        self.rear = node

        self.front = self.front or self.rear


    def dequeue(self):
        if not self.front:
            return Exception
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value


    def peek(self):
        if self.front == None:
            return Exception
        return self.front.value

    def is_empty(self):
        if self.front != None:
            return False
        return True



queue = Queue()
node_a = Node('alpha')
node_b = Node('beta')
# node_c = Node('charlie')
queue.enqueue(node_a)
queue.enqueue(node_b)
# queue.enqueue(node_c)


# stack = Stack()
# stack.push(node_a)
# stack.push(node_b)
# stack.pop()

# print('Stack top value: ',stack.top.value)
# print('Stack next value: ',stack.top.next)
