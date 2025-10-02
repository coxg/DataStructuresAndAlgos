class Heap:

    def __init__(self, *values):
        self._data = []
        for value in values:
            self.push(value)

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def pop(self):
        if not self._data:
            raise TypeError("Heap is empty")

        # start by swapping the first element (guaranteed to be the smallest) with the last element, then removing it
        self._data[0], self._data[len(self._data) - 1] = self._data[len(self._data) - 1], self._data[0]
        result = self._data.pop()

        # swap values down the tree, preferring smaller values, until we get to the bottom - this ensures that min-heap
        # is preserved
        parent_index = 0
        while parent_index < len(self._data) // 2:
            left_index = parent_index * 2 + 1
            right_index = parent_index * 2 + 2

            # short-circuit if heap property already met
            has_right_child = right_index < len(self._data)
            if self._data[parent_index] <= self._data[left_index] and (
                    not has_right_child or self._data[parent_index] <= self._data[right_index]):
                break

            # parent is smaller than left child
            if len(self._data) - 1 < right_index or self._data[left_index] < self._data[right_index]:
                self._data[parent_index], self._data[left_index] = self._data[left_index], self._data[parent_index]
                parent_index = left_index

            # parent is smaller than right child
            else:
                self._data[parent_index], self._data[right_index] = self._data[right_index], self._data[parent_index]
                parent_index = right_index

        return result

    def push(self, value):
        self._data.append(value)
        child_index = len(self._data) - 1

        while child_index > 0:
            parent_index = (child_index - 1) // 2
            parent = self._data[parent_index]
            if value < parent:
                self._data[parent_index], self._data[child_index] = self._data[child_index], self._data[parent_index]
                child_index = parent_index
            else:
                break

    def is_valid(self):
        for i in range(len(self._data) // 2):
            if self._data[i] > self._data[i * 2 + 1]:
                return False
            if len(self._data) > i * 2 + 2 and self._data[i] > self._data[i * 2 + 2]:
                return False
        return True


if __name__ == "__main__":
    import math

    myHeap = Heap(5, 2, 4, 3, 1, 1234, 243, 34, 432, 2, 4, 1234)
    assert myHeap.is_valid()
    prior_value = -math.inf
    for _ in range(len(myHeap)):
        popped_value = myHeap.pop()
        assert popped_value >= prior_value
        assert myHeap.is_valid()
    assert str(myHeap) == "[]"