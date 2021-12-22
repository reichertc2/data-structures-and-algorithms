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


def tree_breadth_first():
    pass

