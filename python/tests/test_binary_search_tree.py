from all_trees.binary_search_tree import BinarySearchTree
from all_trees.binary_tree import BinaryTree
from all_trees.tree_node import Node
import pytest

node_a = Node(15)
node_b = Node(7)
node_c = Node(20)
node_d = Node(1)
node_e = Node(22)


def test_binary_search_tree_a():
    s_tree = BinarySearchTree()
    assert isinstance(s_tree,BinaryTree)

# @pytest.mark.skip('not yet')
def test_binary_search_tree_b():
    tree = BinarySearchTree()
    tree.add(node_a)
    actual = tree.root.value
    expected = 'alpha'

# @pytest.mark.skip('not yet')
def test_binary_search_tree_c():
    tree = BinarySearchTree()
    tree.add(node_a)
    tree.add(node_b)
    actual = tree.root.left_child.value
    expected = 7
    assert actual == expected

# @pytest.mark.skip('not yet')
def test_binary_search_tree_d():
    tree = BinarySearchTree()
    tree.add(node_a)
    tree.add(node_c)
    actual = tree.root.right_child.value
    expected = 20
    assert actual == expected

# @pytest.mark.skip('not yet')
def test_binary_search_tree_e():
    tree = BinarySearchTree()
    tree.add(node_a)
    tree.add(node_b)
    tree.add(node_d)
    actual = tree.root.right_child.left_child.value
    expected = 1
    assert actual == expected

@pytest.mark.skip('not yet')
def test_binary_search_tree_f():
    tree = BinarySearchTree()
    tree.add(node_a)
    tree.add(node_c)
    tree.add(node_e)
    actual = tree.root.right_child.right_child.value
    expected = 22
    assert actual == expected

@pytest.mark.skip('not yet')
def test_binary_search_tree_final():
    pass
