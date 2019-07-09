class Node(object):
    def __init__(self, data, parent_node=None):
        self.data = data
        self.parent_node = parent_node
        self.left_child = None
        self.right_child = None
        self.balance = 0

    def __str__(self):
        return "[%s, %s, %s]" % (self.left_child, self.data, self.right_child)

    def insert(self, data, parent_node):
        """
        inserts data to given node comparing left child and right child
        :param data: value to add
        :param parent_node: Node to which it should add
        :return:
        """
        if data < self.data:
            # go to left side
            if not self.left_child:
                # reached to end of the tree
                self.left_child = Node(data, parent_node)
            else:
                # tree has left leafs so search more
                self.left_child.insert(data, parent_node)
        else:
            # go to left side as data  > self.data
            if not self.right_child:
                # reached to end of the tree
                self.right_child = Node(data, parent_node)
            else:
                # tree has right leafs so search more
                self.right_child.insert(data, parent_node)

        return parent_node

    def traverse_in_order(self):
        if self.left_child:
            self.left_child.traverse_in_order()

        print(self.data)

        if self.right_child:
            self.right_child.traverse_in_order()

    def get_max(self):
        """
        Gives maximum value present in leafs of all nodes
        :return: data
        """
        if not self.right_child:
            # reached to right end return the value
            return self.data
        else:
            # not yet reached to right, return the value of right_child from next node
            return self.right_child.get_max()

    def get_min(self):
        """
        Gives minimum  value present in leafs of all nodes
        :return: data
        """
        if not self.left_child:
            # reached to left end return the value
            return self.data
        else:
            # not yet reached to left, return the value of left_child from next node
            return self.left_child.get_min()


