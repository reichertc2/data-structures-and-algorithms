# ---- Example Psuedo Code ----

# ALGORITHM breadthFirst(root)
# // INPUT  <-- root node
# // OUTPUT <-- front node of queue to console

#   Queue breadth <-- new Queue()
#   breadth.enqueue(root)

#   while ! breadth.is_empty()
#     node front = breadth.dequeue()
#     OUTPUT <-- front.value

#     if front.left is not NULL
#       breadth.enqueue(front.left)

#     if front.right is not NULL
#       breadth.enqueue(front.right)

from stack_and_queue.stack_and_queue import Queue
from all_trees.binary_tree import BinaryTree
from all_trees.tree_node import Node


def tree_breadth_first(tree):
    queue = Queue()
    queue.front == tree.root
    # print(tree.root.value)
    tree_list = []
    temp = queue.front
    while temp:
        item = queue.dequeue()
        tree_list.append(item.value)
        if temp.left_child != None:
            queue.enqueue(temp.left_child)

        if temp.right_child != None:
            queue.enqueue(temp.right_child)

    if temp is None:
        return None
    return tree_list




node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
tree = BinaryTree()
tree.root = node_a

