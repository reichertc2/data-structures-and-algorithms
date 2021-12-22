from code_challenges.tree_breadth_first.tree_breadth_first import tree_breadth_first
from all_trees.binary_tree import BinaryTree
from all_trees.tree_node import Node
import pytest

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')

# @pytest.mark.skip(reason='not yet')
def test_tree_breadth_first_a():
    tree = BinaryTree()
    assert tree_breadth_first(tree) == None

@pytest.mark.skip(reason='not yet')
def test_tree_breadth_first_b():
    tree = BinaryTree()
    tree.root = Node('a')
    actual = tree_breadth_first(tree)
    expected = ['a']
    assert actual == expected
