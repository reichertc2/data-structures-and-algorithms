from all_trees.tree_node import Node
from all_trees.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    def add(self,value):
        if self.root is None:
            self.root = value
        def walk(new_node):
            if self.root.value > value.value:
                print('walk left value.value:',value.value)
                self.root.left_child = value
            else:
                print('walk right value.value:',value.value)
                self.root.right_child = value

        walk(value)


    def contians(self):
        pass



node_a = Node(15)
node_b = Node(7)
node_c = Node(20)
node_d = Node(1)
node_e = Node(22)

tree = BinarySearchTree()
tree.add(node_a)
tree.add(node_c)
tree.add(node_e)

