from all_trees.tree_node import Node
from all_trees.binary_tree import BinaryTree
import pytest

node_a = Node('alpha')
node_b = Node('bravo')
node_c = Node('charlie')

# @pytest.mark.skip('not yet')
def test_binary_tree_a():
    assert BinaryTree()
    assert BinaryTree.pre_order
    assert BinaryTree.in_order
    assert BinaryTree.post_order
    assert Node()

def test_binary_tree_b():
    tree = BinaryTree()
    assert tree.root == None

@pytest.mark.skip('not yet')
def test_binary_tree_c():
    tree = BinaryTree()
    tree.root.value = 'alpha'
    assert tree.pre_order() == 'alpha'


@pytest.mark.skip('not yet')
def test_binary_tree_final():
    tree = BinaryTree()
    tree.root.value = 'alpha'
    tree.root.left_child.value = 'bravo'
    tree.root.right_child.value = 'charlie'
    actual = tree.pre_order()
    expected = ['alpha','bravo','charlie']
    assert actual == expected
