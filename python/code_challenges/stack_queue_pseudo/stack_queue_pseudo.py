from stack_and_queue.stack_and_queue import Node, Stack



class PseudoQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self,node = None):
        if self.stack_in.top != None:
            # temp =
            pass

        if self.stack_in.top == None:
            self.stack_in = node

    def dequeue(self):
        pass




pseudo_queue = PseudoQueue()
# print('pseudo_code: ',pseudo_queue.front)
