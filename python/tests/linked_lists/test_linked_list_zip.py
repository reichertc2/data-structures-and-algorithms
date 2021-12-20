from code_challenges.linked_list_zip.linked_list_zip import linked_list_zip
from linked_list.list import LinkedList, Node
import pytest



def test_linked_list_zip():
    assert linked_list_zip

# @pytest.mark.skip(reason='not yet')
def test_linked_list_zip_a():
    l_list_a = LinkedList()
    l_list_b = LinkedList()
    l_list_a.append(Node('A'))
    l_list_a.append(Node('B'))
    l_list_a.append(Node('C'))
    l_list_b.append(None)
    linked_list_zip(l_list_a, l_list_b)
    assert l_list_a.head.next.value == None

# @pytest.mark.skip(reason='not yet')
def test_linked_list_zip_b():
    l_list_a = LinkedList()
    l_list_b = LinkedList()
    l_list_a.append(Node('A'))
    l_list_a.append(Node('B'))
    l_list_a.append(Node('C'))
    actual = linked_list_zip(l_list_a, l_list_b)
    expected = l_list_a
    assert actual == expected

# @pytest.mark.skip(reason='not yet')
def test_linked_list_zip_c():
    l_list_a = LinkedList()
    l_list_b = LinkedList()
    l_list_a.append(Node('A'))
    l_list_a.append(Node('B'))
    l_list_a.append(Node('C'))
    l_list_b.append(Node('1'))
    linked_list_zip(l_list_a, l_list_b)
    actual = l_list_a.head.next.value.value
    expected = '1'
    assert actual == expected

# @pytest.mark.skip(reason='not yet')
def test_linked_list_zip_d():
    l_list_a = LinkedList()
    l_list_b = LinkedList()
    l_list_a.append(Node('A'))
    l_list_a.append(Node('B'))
    l_list_a.append(Node('C'))
    l_list_b.append(Node('1'))
    l_list_b.append(Node('2'))
    linked_list_zip(l_list_a, l_list_b)
    actual = l_list_a.head.next.next.next.value.value
    expected = '2'
    assert actual == expected

# @pytest.mark.skip(reason='not yet')
def test_linked_list_zip_final():
    l_list_a = LinkedList()
    l_list_b = LinkedList()
    l_list_a.append(Node('A'))
    l_list_a.append(Node('B'))
    l_list_a.append(Node('C'))
    l_list_b.append(Node('1'))
    l_list_b.append(Node('2'))
    l_list_b.append(Node('3'))
    linked_list_zip(l_list_a, l_list_b)
    actual = l_list_a.head.next.next.next.next.next.value.value
    expected = '3'
    assert actual == expected
