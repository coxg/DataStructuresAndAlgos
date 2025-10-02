from LinkedList import LinkedList
from HashMap import HashMap

class OrderedHashMap:

    def __init__(self):
        self._keys = LinkedList()
        self._data = HashMap()  # keys are keys, values are (value, key_node)

    def __setitem__(self, key, value):
        if key not in self._data:
            key_node = self._keys.add_last(key)
        else:
            _, key_node = self._data[key]
        self._data[key] = value, key_node

    def __getitem__(self, item):
        return self._data[item][0]

    def __str__(self):
        return "{" + ", ".join(repr(key) + ": " + repr(self._data[key][0]) for key in self._keys) + "}"

    def __delitem__(self, key):
        key_node = self._data[key][1]
        key_node.prior_node.next_node = key_node.next_node
        key_node.next_node.prior_node = key_node.prior_node
        del self._data[key]


if __name__ == "__main__":
    ordered_hash_map = OrderedHashMap()
    ordered_hash_map["a"] = 0
    assert ordered_hash_map["a"] == 0

    ordered_hash_map["b"] = 1
    ordered_hash_map["c"] = 2
    ordered_hash_map["d"] = 3
    assert str(ordered_hash_map) == "{'a': 0, 'b': 1, 'c': 2, 'd': 3}"

    del ordered_hash_map["b"]
    assert str(ordered_hash_map) == "{'a': 0, 'c': 2, 'd': 3}"
