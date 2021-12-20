class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, next):
        self.head = Node(next, self.head)

    def includes(self, value=None):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += '{ ' + current.value + ' } -> '
            current = current.next
        output += 'NULL'
        return output

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

    def insert_before(self,value,new_value):
        if self.head is None:
            return Exception('empty list')
        if self.head.value == value:
            self.head = Node(new_value,self.head)
            return

        current = self.head

        while current:
            if current.next and current.next.value == value:
                current.next = Node(new_value,current.next)
                break
            current.next
        raise Exception('no before value')


    def insert_after(self, after_node, new_node):
        # print(' after this node: ',after_node)
        # print(' new node: ',new_node)
        if after_node is None:
            return None
        old_node =  Node(after_node)

        # print(' Old Node: value',old_node.next)
        inserted_node = Node(new_node)
        # print(' New Node: value',inserted_node.value)
        old_node.next = inserted_node.value
        inserted_node.next = after_node
        # print(' New Node: next',inserted_node.next)


        inserted_node.value = after_node
        # print(' to inserted_node.value',inserted_node.value)

        after_node = inserted_node
        # print('linked_list.value: ',after_node.value)
        # print(' after_node.next: ',after_node.next)

        return after_node.value



    def kth_from_end(self, k_element):
        length_count = 0
        temp = self.head
        while (temp):
            temp = temp.next
            length_count += 1
        if length_count < k_element:
            return IndexError
        elif k_element < 0:
            return None
        else:
            index_from_end = k_element
            index = length_count - index_from_end
            item = self.head
            for x in range(index-1):
                # item += '.next'
                if item.next:
                    item = item.next

                    # print(item)
            #     # print(return_value)
            # item.next.value
            # stripped_item = item.strip('"', "")
            # print(item.value)
            return item.value


linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)

# print('index 0: ', linked_list.head.value)
# print('index 1: ', linked_list.head.next.value)
# print('index 2: ', linked_list.head.next.next.value)
# print('index 3: ', linked_list.head.next.next.next.value)

# test = linked_list.kth_from_end(0)
# print(linked_list)



linked_list.insert_after(3, 4)

# linked_list.insert_after(None,6)

# print('index 0: ', linked_list.head.value)
# print('index 1: ', linked_list.head.next.value)
# print('index 2: ', linked_list.head.next.next.value)
# print('index 3: ', linked_list.head.next.next.next.value)
# print('index 4: ', linked_list.head.next.next.next.next.value)

# print('index 0: ', linked_list.head.value)
# print('index 1: ', linked_list.head.next.value)
# print('index 2: ', linked_list.head.next.next.value)
# print('index 3: ', linked_list.head.next.next.next.value)
# print('index 4: ', linked_list.head.next.next.next.next.value)

print('End of Line...')
