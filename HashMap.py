class Unallocated:
    def __eq__(self, other):
        return type(other) == Unallocated


class Tombstone:
    def __eq__(self, other):
        return type(other) == Tombstone


class HashMap:

    def __init__(self):
        self._keys = [Unallocated() for _ in range(8)]
        self._values = [Unallocated() for _ in range(8)]
        self._count = 0  # number of populated key/value pairs
        self._consumed_space = 0  # number of populated key/value pairs and tombstones

    def __setitem__(self, key, value):
        for offset in range(len(self._keys)):
            check_index = (hash(key) + offset) % len(self._keys)
            check_key = self._keys[check_index]

            # overwrite found value for key
            if check_key == key:
                self._values[check_index] = value
                return

            # insert new key/value
            if check_key == Unallocated():
                self._keys[check_index] = key
                self._values[check_index] = value
                self._consumed_space += 1
                self._count += 1

                if self._consumed_space > len(self._keys) / 2:
                    self._resize()

                return

    def __getitem__(self, item):
        i = self._get_index(item)
        return self._values[i]

    def __delitem__(self, key):
        i = self._get_index(key)
        self._keys[i] = Tombstone()
        self._values[i] = Tombstone()
        self._count -= 1

    def __len__(self):
        return self._count

    def __str__(self):
        return "{" + ", ".join(str(key) + ": " + str(value) for key, value in zip(self.keys, self.values)) + "}"

    def _get_index(self, key):
        for offset in range(len(self._keys)):
            check_index = (hash(key) + offset) % len(self._keys)
            if self._keys[check_index] == key:
                return check_index
        raise KeyError(key)

    def _resize(self):
        old_keys = self._keys
        old_values = self._values

        new_size = len(self._keys) * 2
        self._keys = [Unallocated() for _ in range(new_size)]
        self._values = [Unallocated() for _ in range(new_size)]
        self._count = 0  # gets repopulated when setting items below
        self._consumed_space = 0  # gets repopulated when setting items below

        for key, value in zip(old_keys, old_values):
            self[key] = value

    @property
    def keys(self):
        return [key for key in self._keys if key not in (Unallocated(), Tombstone())]

    @property
    def values(self):
        return [value for key, value in zip(self._keys, self._values) if key not in (Unallocated(), Tombstone())]

if __name__ == "__main__":
    hashMap = HashMap()
    hashMap[1] = 2
    assert hashMap.keys == [1]
    assert hashMap.values == [2]
    assert hashMap[1] == 2

    hashMap[1] = 3
    assert hashMap.values == [3]
    assert hashMap[1] == 3

    hashMap["test"] = "success"
    assert hashMap["test"] == "success"

    del hashMap[1]
    assert hashMap.keys == ["test"]
    assert hashMap.values == ["success"]