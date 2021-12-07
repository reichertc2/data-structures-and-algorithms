class Node:
    def __init__(self, head,next= None):
        self.head = head
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self,item):
        # print(str(self.head.next))
        # print(item)
        self.head = Node(item,self.head)
        return self.head
        # print(str(self.head.next))

    def append(self,item):
        end_insert = Node(item)
        # print(end_insert.head.head)
        if self.head is None:
            self.head = end_insert
            return
        end = self.head
        while (end.next):
            end = end.next
        end.next = end_insert
        # print(end.next.head.head)

    def insert_before(self,item, placement):
        new_node = Node(item)
        print(placement.head)
        if item.head == placement.head:
            print('True')





    def insert_after(self):
        pass

test = LinkedList()
node_a = Node('gizmo')
node_b = Node('gabriel')
node_c = Node('trevor')

# print(node_a.head)


# print(test.next)
test.insert(node_a)
test.insert(node_b)
# print(test.head.head.head)
# print(test.head.head)
# print(test.head.next)
test.append(node_c)
# print(len(test))
# print(test.head.next.next)

test.insert_before(node_a,node_b)

