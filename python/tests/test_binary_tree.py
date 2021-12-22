from all_trees.tree_node import Node
from all_trees.binary_tree import BinaryTree
from all_trees.binary_search_tree import BinarySearchTree
import pytest

node_a = Node('alpha')
node_b = Node('bravo')
node_c = Node('charlie')
node_d = Node('delta')

# @pytest.mark.skip('not yet')
def test_binary_tree_a():
    assert BinaryTree()
    assert BinaryTree.pre_order
    assert BinaryTree.in_order
    assert BinaryTree.post_order
    assert Node()

def test_binary_tree_pre_order_a():
    tree = BinaryTree()
    assert tree.root == None

# @pytest.mark.skip('not yet')
def test_binary_tree_pre_order_b():
    tree = BinaryTree(node_a)
    actual = tree.pre_order()
    expected = ['alpha']
    assert actual == expected

# @pytest.mark.skip('not yet')
def test_binary_tree_pre_order_c():
    tree = BinaryTree(node_a)
    tree.root.left_child = node_b
    actual = tree.pre_order()
    expected = ['alpha','bravo']
    assert actual == expected

@pytest.mark.skip('not yet')
def test_binary_tree_pre_order_final():
    tree = BinaryTree(node_a)
    tree.root.left_child = node_b
    tree.root.right_child = node_c
    tree.root.left_child.left_child = node_d
    actual = tree.pre_order()
    expected = ['alpha','bravo','delta','charlie']
    assert actual == expected

# @pytest.mark.skip('not yet')
def test_binary_tree_in_order_a():
    tree = BinaryTree(node_a)
    actual = tree.in_order()
    expected = ['alpha']
    assert actual == expected

@pytest.mark.skip('not yet')
def test_binary_tree_in_order_b():
    tree = BinaryTree(node_a)
    tree.root.left_child = node_b
    actual = tree.in_order()
    expected = ['bravo','alpha']
    assert actual == expected

@pytest.mark.skip('not yet')
def test_binary_tree_in_order_final():
    tree = BinaryTree(node_a)
    tree.root.left_child = node_b
    tree.root.right_child = node_c
    actual = tree.in_order()
    expected = ['bravo','alpha','charlie']
    assert actual == expected


@pytest.mark.skip('not yet')
def test_binary_tree_post_order_a():
    tree = BinaryTree(node_a)
    actual = tree.post_order()
    expected = ['alpha']
    assert actual == expected

@pytest.mark.skip('not yet')
def test_binary_tree_post_order_b():
    tree = BinaryTree(node_a)
    tree.root.left_child = node_b
    actual = tree.post_order()
    expected = ['bravo','alpha']
    assert actual == expected

# @pytest.mark.skip('not yet')
def test_binary_tree_post_order_final():
    tree = BinaryTree(node_a)
    tree.root.left_child = node_b
    tree.root.right_child = node_c
    actual = tree.post_order()
    expected = ['bravo','charlie','alpha']
    assert actual == expected
