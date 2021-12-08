class Node:
    def __init__(self, value, next=0):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, next):
        self.head = Node(next, self.head)

    def includes(self, value=None):
        for value in self.head.value:
            if value == self.head:
                return True
            elif value == self.head.next:
                return True
        return False

    def __str__():
        pass

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
        print(placement.value)
        if item.value == placement.value:
            print('True')
            return True

    def insert_after(self):
        pass

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


# linked_list = LinkedList()
# linked_list.insert(2)
# linked_list.insert(8)
# linked_list.insert(3)
# linked_list.insert(1)

# print('index 0: ', linked_list.head.value)
# print('index 1: ', linked_list.head.next.value)
# print('index 2: ', linked_list.head.next.next.value)
# print('index 3: ', linked_list.head.next.next.next.value)

# test = linked_list.kth_from_end(0)
# print(test)
