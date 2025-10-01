class Node:
    def __init__(self, value, next_node):
        self.value = value
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
        return "[" + ", ".join(str(elem) for elem in self) + "]"

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
        node = Node(element, self.head)
        self.head = node

        if not self.tail:
            self.tail = node

    def add_last(self, element):
        node = Node(element, None)
        if self.tail:
            self.tail.next_node = node
        self.tail = node

        if not self.head:
            self.head = node


if __name__ == "__main__":
    myLinkedList = LinkedList(1, 2, 3, 4, 5)
    assert str(myLinkedList) == "[1, 2, 3, 4, 5]"

    myLinkedList.reverse()
    assert str(myLinkedList) == "[5, 4, 3, 2, 1]"

    myLinkedList.reverse()
    assert str(myLinkedList) == "[1, 2, 3, 4, 5]"

    myLinkedList.add_last(6)
    assert str(myLinkedList) == "[1, 2, 3, 4, 5, 6]"

    myLinkedList.add_first(0)
    assert str(myLinkedList) == "[0, 1, 2, 3, 4, 5, 6]"