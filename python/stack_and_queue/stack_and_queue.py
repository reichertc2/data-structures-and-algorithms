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

    def enqueue(self, value = None):

        # print('enqueue value: ',value)
        if self.front != None:
            temp = self.front
            while (temp) != None:
                print('before while temp value: ',temp.value)
                temp = value.next

                print('after while temp.value: ', temp)
        if self.front == None:
            self.front = value
            self.next = None
            # print('in if self.front == None: ',self.front.value)

        # self.front = value
        # return self.front
        print('new self.front.value: ',self.front.value)



    def dequeue(self):
        pass
    def peek(self):
        if self.top == None:
            return Exception
        return self.top.value

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
