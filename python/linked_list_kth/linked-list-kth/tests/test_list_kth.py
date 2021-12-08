import pytest
from linked_list_kth.list_kth import Node, LinkedList


# @pytest.mark.skip(reason='not today')
def test_code_challenge():
    assert Node
    assert LinkedList


# @pytest.mark.skip(reason='not yet')
def test_LinkedList_index_error():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)
    assert  linked_list.kth_from_end(6) == IndexError


# @pytest.mark.skip(reason='not yet')
def test_LinkedList_a():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)
    assert  linked_list.kth_from_end(1) == 8

# @pytest.mark.skip(reason='not yet')
def test_LinkedList_b():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)
    assert  linked_list.kth_from_end(-1) == None

# @pytest.mark.skip(reason='not yet')
def test_LinkedList_c():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)
    assert  linked_list.kth_from_end(3) == 1



# @pytest.mark.skip(reason='not yet')
def test_LinkedList_final():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)
    assert  linked_list.kth_from_end(0) == 2
    assert  linked_list.kth_from_end(1) == 8
    assert  linked_list.kth_from_end(6) == IndexError

