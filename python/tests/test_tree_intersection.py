from code_challenges.tree_intersection.tree_intersection import tree_intersection
from all_trees.tree_node import Node
from all_trees.binary_tree import BinaryTree
import pytest

node_a = Node(1)
node_b = Node(15)
node_c = Node(88)
node_d = Node(3)
node_e = Node(21)
node_f = Node(5)
node_g = Node(8)
node_h = Node(13)



# @pytest.mark.skip(reason='not yet')
def test_tree_intersection_a():
    assert tree_intersection

# @pytest.mark.skip(reason='not yet')
def test_tree_intersection_a():
    tree_a = BinaryTree(Node(1))
    tree_a.root.left_child = node_b
    tree_a.root.right_child = Node(15)
    tree_a.root.left_child.left_child = node_d
    tree_b = BinaryTree(Node(1))
    tree_b.root.left_child = node_e
    tree_b.root.right_child = Node(15)
    tree_b.root.left_child.left_child = node_a
    actual = tree_intersection(tree_a,tree_b)
    expected = {1,15}
    assert actual == expected

