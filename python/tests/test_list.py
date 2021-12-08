from linked_list.list import  Node, LinkedList
import pytest


# Node class testing

# @pytest.mark.skip(reason='not quite time')
def test_Node_a():
    assert Node('first go')

# @pytest.mark.skip(reason='not quite time')
def testNode_b():
    node = Node('first go')
    actual = node.value
    expected = 'first go'
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def testNode_c():
    node = Node('first go', 'second')
    actual = node.next
    expected = 'second'
    assert actual == expected

@pytest.mark.skip(reason='not quite time')
def testNode_d():
    node = Node('first go')
    actual = node.next
    expected = None
    assert actual == expected

# LinkeList class testing

# @pytest.mark.skip(reason='not quite time')
def test_LinkedList_a():
    assert LinkedList.insert
    assert LinkedList.includes
    assert LinkedList.__str__

# @pytest.mark.skip(reason='not quite time')
def test_LinkedList_b():
    node = LinkedList()
    expected =  None
    actual = node.head
    assert expected == actual

# @pytest.mark.skip(reason='not quite time')
def test_LinkedList_insert_a():
    linked_list = LinkedList()
    linked_list.insert('gizmo')
    expected = linked_list.head
    actual = 'gizmo'
    assert expected == actual

@pytest.mark.skip(reason='not quite time')
def test_LinkedList_insert_a():
    linked_list = LinkedList()
    linked_list.insert('gizmo')
    expected = linked_list.head
    actual = 'gizmo'
    assert expected == actual


@pytest.mark.skip(reason='not quite time')
def test_LinkedList_includes_a():
    linked_list = LinkedList()
    linked_list.insert('gizmo')
    linked_list.insert('gabriel')
    actual = linked_list.includes('gizmo')
    expected = True
    assert expected == actual
