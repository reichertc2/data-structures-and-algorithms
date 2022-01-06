# from stack_and_queue.stack_and_queue import Queue

class Node:
    def __init__(self,value=None,left_child=None,right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

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

class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def pre_order(self):
        pre_order_list = []

        def walk(root):

            if root is None:
                return

            if root:
                pre_order_list.append(root.value)
                walk(root.left_child)
                walk(root.right_child)

        walk(self.root)

        return pre_order_list


    def in_order(self):

        in_order_list = []

        def walk(root):

            if root is None:
                return

            if root:
                walk(root.left_child)
                in_order_list.append(root.value)
                walk(root.right_child)

        walk(self.root)

        return in_order_list


    def post_order(self):

        post_order_list = []

        def walk(root):

            if root is None:
                return

            if root:
                walk(root.left_child)
                walk(root.right_child)
                post_order_list.append(root.value)

        walk(self.root)



        return post_order_list


    def find_maximum_value(self):
        if self.root is None:
            return None
        tree_list = self.pre_order()

        return max(tree_list)


def tree_fizz_buzz(tree):

    queue = Queue()
    queue.enqueue(tree.root.value)

    # print(queue.front.value.value)
    # queue.front.next = tree.root.left_child
    while queue.front:
        # queue.front.next = tree.root.left_child
        # print(queue.front.value.value)

        node = queue.dequeue()

        print(node.left_child.value)
        # print(node.value)
        # queue.enqueue(node.left_child)


tree = BinaryTree()
tree.root = Node(3)
tree.root.left_child = Node(5)
tree.root.right_child = Node(15)
tree.root.left_child.left_child = Node(17)




tree_fizz_buzz(tree)
