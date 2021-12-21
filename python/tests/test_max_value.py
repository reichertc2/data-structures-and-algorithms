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

def test_max_value_a():
    tree = BinaryTree()
    assert tree.find_maximum_value() == None

def test_max_value_b():
    tree = BinaryTree(node_1)
    assert tree.find_maximum_value() == 1

def test_max_value_c():
    tree = BinaryTree(node_1)
    tree.root.left_child = node_2
    assert tree.find_maximum_value() == 16

def test_max_value_c():
    tree = BinaryTree(node_1)
    tree.root.left_child = node_2
    tree.root.right_child = node_3
    tree.root.left_child.right_child = node_4
    assert tree.find_maximum_value() == 22
