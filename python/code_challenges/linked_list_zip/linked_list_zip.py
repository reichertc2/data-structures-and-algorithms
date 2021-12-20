from linked_list.list import LinkedList, Node

def linked_list_zip(l_list_a,l_list_b):
    current_a = l_list_a.head
    current_b = l_list_b.head
    while current_a and current_b:
        next_a = current_a.next
        next_b = current_b.next
        current_a.next = current_b
        if next_a:
            current_b.next = next_a
        current_a = next_a
        current_b = next_b
    return l_list_a if l_list_a.head else l_list_b


l_list_a = LinkedList()
l_list_b = LinkedList()
l_list_a.append(Node('A'))
l_list_a.append(Node('B'))
l_list_a.append(Node('C'))

print(l_list_a.head.value)
# print(linked_list_zip(l_list_a, l_list_b))
