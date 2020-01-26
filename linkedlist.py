"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
                Assume the first position is "1".
                Return "None" if position is not in the list."""
        start = 2
        current = self.head
        # check for when a position is less than 1 to avoid errors
        if position == 1:
            return current
        else:
            while start <= position:
                current = current.next
                start += 1

        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
                Assume the first position is "1".
                Inserting at position 3 means between
                the 2nd and 3rd elements."""
        current = self.get_position(position-1)
        val = self.get_position(position)
        current.next = new_element
        current.next.next = val

    def delete(self, value):
        """Delete the first node with a given value."""
        node = self.get_position(value)
        current = self.head
        if value == 1:
            self.head = current.next
        if value > 1 and node.next:
            val = self.get_position(value-1)
            val.next = val.next.next
        if node.next is None:
            val = self.get_position(value - 1)
            val.next = None


