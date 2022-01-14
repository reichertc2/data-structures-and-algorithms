import queue
from hash_table.hash_table import HashTable
from stack_and_queue.stack_and_queue import Queue

from all_trees.tree_node import Node
from all_trees.binary_tree import BinaryTree

# Peer programmed with Chloe Nott


# Create function tree_intersection with arguments of two binary trees
# create new set variable
# create new hashmap
# traverse binary tree populate set
	# breadth first traversal
	# populate values to hashmap at each node
# traverse second tree while utilizing hash.contains() to compare values simultaneously at each Node
	# if contains is true add to new set
# return new set

def tree_intersection(binary_tree_a, binary_tree_b ):
    new_set = set()
    hash_table = HashTable()

# traverse binary tree populate set
	# breadth first traversal
    queue_a = []
    queue_a.insert(0,binary_tree_a.root)
    while queue_a:
        item = queue_a.pop()
        # populate values to hashmap at each node
        hash_table.add(item.value)

        if item.left_child != None:
            queue_a.insert(0,item.left_child)

        if item.right_child != None:
            queue_a.insert(0,item.right_child)

# traverse second tree while utilizing hash.contains() to compare values simultaneously at each Node
    queue_b = []
    queue_b.insert(0,binary_tree_b.root)

    while queue_b:
        item = queue_b.pop()
    # populate values to hashmap at each node
        if hash_table.contains(item.value):
            print('queue_b containsL',item.value)
            new_set.add(item.value)

        if item.left_child != None:
            queue_b.insert(0,item.left_child)

        if item.right_child != None:
            queue_b.insert(0, item.right_child)

	# if contains is true add to new set

    return new_set

node_a = Node(1)
node_b = Node(15)
node_c = Node(88)
node_d = Node(3)
node_e = Node(21)
node_f = Node(5)
node_g = Node(8)
node_h = Node(13)


tree_a = BinaryTree(node_a)
tree_a.root.left_child = node_b
tree_a.root.right_child = node_c
tree_a.root.left_child.left_child = node_d
tree_b = BinaryTree(node_a)
tree_b.root.left_child = node_e
tree_b.root.right_child = node_c
tree_b.root.left_child.left_child = node_f



tree_intersection(tree_a,tree_b )
