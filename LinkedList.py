"""
Add three functions to the LinkedList.  

1. "get_position" returns the element at a certain position.

2. The "insert" function will add an element to a particular
spot in the list.

3. "delete" will delete the first element with that
particular value.

4. "printlist" will add all values of Elements in array

"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        Add new element..
        1. Find the last element 
        2. Add its next to Element object
        :param new_element: <Element>
        :return: None
        """

        # first element will be self.head
        if not self.head:
            # means no items in LinkedList
            self.head = new_element
        else:
            current_element = self.head
            while current_element.next:
                current_element = current_element.next
            current_element.next = new_element

    def get_position(self, position):
        """
        :param position: e.g. 1/2/3/5
        :return: <Element oz>/"None" if position is not in the list
        """
        counter = 1
        current_element = self.head
        while current_element and counter <= position:
            if counter == position:
                return current_element
            current_element = current_element.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements
        :param new_element:  <Element>
        :param position: 1/2/3
        """
        current_element = self.head
        counter = 1
        if position > 1:
            while current_element and counter < position:
                if counter == position - 1:
                    new_element.next = current_element.next
                    current_element.next = new_element
                current_element = current_element.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""

        current_element = self.head
        previous_element = None
        while current_element.next and current_element.value != value:
            previous_element = current_element
            current_element = current_element.next
        if current_element.value == value:
            if previous_element:
                previous_element.next = current_element.next
            else:
                self.head = current_element.next

    def printlist(self):
        """
        Print all values present in Elements of LinkedList
        :return:
        """
        current_element = self.head
        items = []
        while current_element:
            items.append(current_element.value)
            current_element = current_element.next
        return items


# Set up Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

# Setup LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

ll.printlist()
# [1, 2, 3, 4]

# add e5 at 2nd positio
ll.insert(e5, 2)
# [1, 5, 2, 3, 4]

ll.printlist()
# [1, 5, 2, 3, 4]

#remove element whose value is 5
ll.delete(5)
ll.printlist()
# [1, 2, 3, 4]
