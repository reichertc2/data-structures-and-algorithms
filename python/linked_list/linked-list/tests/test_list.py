from linked_list.list import Node, LinkedList
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

# @pytest.mark.skip(reason='not quite time')


def testNode_d():
    node = Node('first go')
    actual = node.next
    expected = None
    assert actual == expected

# LinkeList class testing

# @pytest.mark.skip(reason='not quite time')
def test_LinkedList_a():
    assert LinkedList.insert
    assert LinkedList.include
    assert LinkedList.__str__


def test_LinkedList_b():
    node = LinkedList('value')
    expected = 'value'
    actual = node.value
    assert expected == actual

# @pytest.mark.skip(reason='not quite time')




@pytest.mark.skip(reason='not quite time')
def test_LinkedList_c():
    actual = LinkedList('value')
    expected = 'value'
    assert actual == expected


@pytest.mark.skip(reason='not quite time')
def test_LinkedList_d():
    pass
