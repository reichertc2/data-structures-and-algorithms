from all_trees.tree_node import Node
from all_trees.binary_tree import BinaryTree
import pytest

node_1 = Node(1)
node_2 = Node(16)
node_3 = Node(22)
node_4 = Node(5)


def test_max_initalization():
    tree = BinaryTree()
    assert tree.find_maximum_value
