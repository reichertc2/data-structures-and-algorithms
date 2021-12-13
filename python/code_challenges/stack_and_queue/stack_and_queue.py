class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self, value):
        self.top = value
        return self.top

    def pop(self):
        if self.top:
            old_top = self.top
            self.top = None
            return old_top.value
        if self.top == None:
            return Exception

    def peek(self):
        if self.top == None:
            return Exception
        return self.top.value

    def is_empty(self):
        if self.top != None:
            False
        return True


class Queue:
    def __init__(self, front = None):
        self.front = front

    def enqueue(self, value = None):

        print('enqueue value: ',value.value)
        if self.front == None:
            self.front = value
            self.next = None
            # print('in if self.front == None: ',self.front.value)
        if self.front.value != None:
            temp = self.front
            while (temp) != None:
                print('while temp value: ',temp.value)
                temp = temp.next

                print('while temp.value: ', temp)
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
        pass



queue = Queue()
node_a = Node('alpha')
node_b = Node('beta')
node_c = Node('charlie')
queue.enqueue(node_a)
queue.enqueue(node_b)
queue.enqueue(node_c)
