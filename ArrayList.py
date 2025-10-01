class ArrayList:

    def __init__(self, *inputs):
        self._data = [None for _ in range(8)]
        self._count = 0
        for _input in inputs:
            self.append(_input)

    def __len__(self):
        return self._count

    def _resize(self):
        _newData = [None for _ in range(len(self._data) * 2)]
        for i in range(len(self._data)):
            _newData[i] = self._data[i]
        self._data = _newData

    def append(self, other):
        if self._count == len(self._data):
            self._resize()
        self._data[self._count] = other
        self._count += 1

    def remove(self, index):
        self._validate_index(index)

        for curIndex in range(index, self._count):
            self._data[curIndex] = self._data[curIndex + 1]

        self._count -= 1

    def __str__(self):
        return "[" + ", ".join(str(x) for x in self._data[:self._count]) + "]"

    def __getitem__(self, index):
        self._validate_index(index)
        return self._data[index]

    def _validate_index(self, index):
        if not type(index) == int:
            raise IndexError
        if index >= self._count:
            raise IndexError(f"Index {index} out of bounds")

    def __eq__(self, other):
        try:
            if len(self) != len(other):
                return False
        except TypeError:  # if the other object has no length
            return False

        for i in range(len(other)):
            if self[i] != other[i]:
                return False

        return True


if __name__ == "__main__":

    myArray = ArrayList(1, 2, 3)
    assert str(myArray) == "[1, 2, 3]"
    assert myArray == [1, 2, 3]
    assert myArray[0] == 1

    myArray.append(4)
    assert myArray == [1, 2, 3, 4]

    myArray.remove(1)
    assert myArray == [1, 3, 4]

    myArray.remove(2)
    assert myArray == [1, 3]

    for i in range(1000):
        myArray.append(i)
    assert len(myArray) == 1002