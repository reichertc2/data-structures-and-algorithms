from all_trees.tree_node import Node

class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def pre_order(self):
        pre_order_list = []
        if self.root is None:
            return

        def walk(temp,side=None):
            if temp:
                pre_order_list.append(temp.value)
                return
            if side == 'left':
                if temp.left_child == None:
                    return
                pre_order_list.append(temp.left_child)
                return


        if self.root != None:
            temp = self.root
            walk(temp)
            walk(temp,'left')
            # while temp:
            #     if temp.left_child:

            #         temp = temp.left_child.value
            #         pre_order_list.append(temp)
            #         return
            #     temp = temp.right_child
            #     pre_order_list.append(temp)
            #     return

            return pre_order_list










    def in_order(self):
        pass
    def post_order(self):
        pass
