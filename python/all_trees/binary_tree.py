from all_trees.tree_node import Node

class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def pre_order(self):
        pre_order_list = []

        def walk(temp):

            if temp is None:
                return

            if temp:
                pre_order_list.append(temp.value)


            walk(temp.left_child)
            walk(temp.right_child)

        walk(self.root)

        return pre_order_list


    def in_order(self):

        in_order_list = []

        def walk(temp):

            if temp is None:
                return

            if temp:
                in_order_list.append(temp.value)


            walk(temp.left_child)
            walk(temp.right_child)

        walk(self.root)

        return in_order_list


    def post_order(self):
        pass

    def find_maximum_value(self):
        if self.root is None:
            return None
        tree_list = self.pre_order()

        return max(tree_list)
