from linked_list_insertions.insertions import LinkedList, Node
import pytest

node_a = Node('gizmo')
node_b = Node('gabriel')
node_c = Node('trevor')


# @pytest.mark.skip("todo")
def test_code_challenge_connection():
    assert LinkedList.append
    assert LinkedList.insert_before
    assert LinkedList.insert_after

# @pytest.mark.skip("todo")
def test_insert_a():
    # node_a = Node('gizmo')
    linked_list = LinkedList()
    linked_list.insert(node_a)
    expected = 'gizmo'
    assert linked_list.head.head.head =='gizmo'
    assert linked_list.head.next == None

# @pytest.mark.skip("todo")
def test_insert_b():
    # node_a = Node('gizmo')
    # node_b = Node('gabriel')
    linked_list = LinkedList()
    linked_list.insert(node_a)
    linked_list.insert(node_b)
    actual = linked_list.head.next.head.head
    expected = 'gizmo'
    assert expected == actual

# @pytest.mark.skip("todo")
def test_LinkedList_append_a():
    linked_list = LinkedList()
    linked_list.append(node_c)
    assert node_c.head == 'trevor'

# @pytest.mark.skip("todo")
def test_LinkedList_append_b():
    linked_list = LinkedList()
    linked_list.append(node_c)
    assert linked_list.head.head.next == None

# @pytest.mark.skip("todo")
def test_LinkedList_append_c():
    linked_list = LinkedList()
    linked_list.insert(node_a)
    linked_list.append(node_c)
    expected = 'trevor'
    actual = linked_list.head.next.head.head
    assert expected == actual

# @pytest.mark.skip("todo")
def test_LinkedList_append_d():
    linked_list = LinkedList()
    linked_list.insert(node_a)
    linked_list.insert(node_b)
    linked_list.append(node_c)
    expected = 'trevor'
    actual = linked_list.head.next.next.head.head
    assert expected == actual

# @pytest.mark.skip("todo")
def test_LinkedList_insert_before_a():
    linked_list = LinkedList()
    assert linked_list.insert_before(node_a,1) == 1



@pytest.mark.skip("todo")
def test_LinkedList_insert_afer_a():
    pass
