from all_trees.tree_node import Node

class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def pre_order(self):
        pre_order_list = []

        def walk(root):

            if root is None:
                return

            if root:
                pre_order_list.append(root.value)
                walk(root.left_child)
                walk(root.right_child)

        walk(self.root)

        return pre_order_list


    def in_order(self):

        in_order_list = []

        def walk(root):

            if root is None:
                return

            if root:
                walk(root.left_child)
                in_order_list.append(root.value)
                walk(root.right_child)

        walk(self.root)

        return in_order_list


    def post_order(self):

        post_order_list = []

        def walk(root):

            if root is None:
                return

            if root:
                walk(root.left_child)
                walk(root.right_child)
                post_order_list.append(root.value)

        walk(self.root)



        return post_order_list


    def find_maximum_value(self):
        if self.root is None:
            return None
        tree_list = self.pre_order()

        return max(tree_list)
