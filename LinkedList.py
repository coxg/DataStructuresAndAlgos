class Node:
    def __init__(self, value, prior_node, next_node):
        self.value = value
        self.prior_node = prior_node
        self.next_node = next_node


class LinkedList:

    def __init__(self, *elements):
        self.head = None
        self.tail = None
        for elem in elements:
            self.add_last(elem)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node

    def __str__(self):
        return "[" + ", ".join(repr(elem) for elem in self) + "]"

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node

        self.head, self.tail = self.tail, self.head

    def add_first(self, element):
        node = Node(element, None, self.head)
        if self.head:
            self.head.prior_node = node
        self.head = node

        if not self.tail:
            self.tail = node

        return node

    def add_last(self, element):
        node = Node(element, self.tail, None)
        if self.tail:
            self.tail.next_node = node
        self.tail = node

        if not self.head:
            self.head = node

        return node


if __name__ == "__main__":
    linked_list = LinkedList(1, 2, 3, 4, 5)
    assert str(linked_list) == "[1, 2, 3, 4, 5]"

    linked_list.reverse()
    assert str(linked_list) == "[5, 4, 3, 2, 1]"

    linked_list.reverse()
    assert str(linked_list) == "[1, 2, 3, 4, 5]"

    linked_list.add_last(6)
    assert str(linked_list) == "[1, 2, 3, 4, 5, 6]"

    linked_list.add_first(0)
    assert str(linked_list) == "[0, 1, 2, 3, 4, 5, 6]"