from stack_and_queue.stack_and_queue import Node, Stack



class PseudoQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def dequeue(self,node = None):
        while not self.stack_in.is_empty():
            self.stack_out.push(self.stack_in.pop())
        if self.stack_out.is_empty():
            raise Exception
        return self.stack_out.pop()

        # if self.stack_in.top != None:
        #     # temp =
        #     pass

        # if self.stack_in.top == None:
        #     self.stack_in = node

    def enqueue(self,value):
        while not self.stack_out.is_empty:
            self.stack_in.push(self.stack_out.pop())
        self.stack_in.push(value)

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def peek(self):
        if self.is_empty():
            raise Exception
        while not self.stack_in.is_empty():
            self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()



pseudo_queue = PseudoQueue()
# print('pseudo_code: ',pseudo_queue.front)
