class Node(object):
    def __init__(self, value):
        self.left_node = None
        self.right_node = None
        self.value = value

    def __str__(self):
        return "[%s, %s, %s]" % (self.left_node, self.value, self.right_node)

    def insertValue(self, new_value):
        """
        1. if current Node doesnt have value then assign to self
        2. new_value lower than current Node's value then go left
        2. new_value greater than current Node's value then go right
        :return:
        """
        if self.value:
            if new_value < self.value:
                # add to left
                if self.left_node is None:  # reached start add value to start
                    self.left_node = Node(new_value)
                else:
                    self.left_node.insertValue(new_value)  # search
            elif new_value > self.value:
                # add to right
                if self.right_node is None:  # reached end add value to end
                    self.right_node = Node(new_value)
                else:
                    self.right_node.insertValue(new_value)  # search
        else:
            self.value = new_value

    def findValue(self, value_to_find):
        """
        1. value_to_find is equal to current Node's value then found
        2. if value_to_find is lower than Node's value then go to left
        3. if value_to_find is greater than Node's value then go to right
        """
        if value_to_find == self.value:
            return "Found"
        elif value_to_find < self.value and self.left_node:
            return self.left_node.findValue(value_to_find)
        elif value_to_find > self.value and self.right_node:
            return self.right_node.findValue(value_to_find)
        return "Not Found"

    def printTree(self):
        """
        Nodes will be in sequence
        1. Print LHS items
        2. Print value of node
        3. Print RHS items
        """
        if self.left_node:
            self.left_node.printTree()
        print(self.value),
        if self.right_node:
            self.right_node.printTree()

    def isEmpty(self):
        return self.left_node == self.right_node == self.value == None


def main():
    root_node = Node(12)
    root_node.insertValue(6)
    root_node.insertValue(3)
    root_node.insertValue(7)

    # should return 3 6 7 12
    root_node.printTree()

    # should return found
    root_node.findValue(7)
    # should return found
    root_node.findValue(3)
    # should return Not found
    root_node.findValue(24)

if __name__ == '__main__':
    main()
