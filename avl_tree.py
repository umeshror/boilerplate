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


class BalancedTree(object):
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if not self.root_node:
            parent_node = Node(data, None)
            self.root_node = parent_node
        else:
            parent_node = self.root_node.insert(data, self.root_node)

        self.rebalance_tree(parent_node)

    def rebalance_tree(self, parent_node):
        """
              [height] (value)


                [2](20)
                  /    \
        [0] (10)       (40) [1]
                        /  \
                [0] (30)   (50) [0]

         mod of  | height(left sub tree) - height (right sub tree) | <= 1
            mod of

        :param parent_node:
        :return:
        """
        self.set_balance(parent_node)
        if parent_node.balance < -1:
            if self.height(parent_node.left_child.left_child) >= self.height(parent_node.left_child.right_child)
                parent_node = self.rotate_right(parent_node)
            else:
                parent_node = self.rotate_left_right(parent_node)
        elif parent_node.balance > 1
            if self.height(parent_node.right_child.right_child) >= self.height(parent_node.right_child.left_child):
                parent_node = self.rotate_left(parent_node)
            else:
                parent_node = self.rotate_right_left(parent_node)

        if parent_node.parent_node is not None:
            self.rebalance_tree(parent_node.parent_node)
        else:
            self.root_node = parent_node


    def rotate_left_right(self, node):
        node.left_child = self.rotate_left(node)
        return self.rotate_right(node)

    def rotate_right_left(self, node):
        node.right_child = self.rotate_right(node)
        return self.rotate_left(node)

    def rotate_left(self, node):
        temp = node.right_child
        temp.parent_node = node.parent_node

        node.right_child = temp.left_child

        if node.right_child is not None:
            if temp.parent_node.right_child == node:
                temp.parent_node.right_child = temp
            else:
                temp.parent_node.left_child = temp
        self.set_balance(node)
        self.set_balance(temp)

        return temp

    def rotate_right(self, node):
        temp = node.left_child
        temp.parent_node = node.parent_node

        node.left_child = temp.right_child

        if node.left_child is not None:
            if temp.parent_node.left_child == node:
                temp.parent_node.left_child = temp
            else:
                temp.parent_node.right_child = temp
        self.set_balance(node)
        self.set_balance(temp)

        return temp


    def set_balance(self, node):

        node.balance = (self.height(node.left_child) - self.height(node.right_child))

    def height(self, node):
        if not node:
            # no node present returns default value -1
            return -1
        else:
            # 1 + max_height
            # e.g 1 + max(-1, -1) = 0
            # e.g 1 + max(0, -1) = 2
            return 1 + max(self.height(node.left_child), self.height(node.right_child))
