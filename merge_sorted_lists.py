def merge_two_sorted_lists(l1: list[object], l2: list[object]):
    result = []
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(l1) and pointer2 < len(l2):
        val1 = l1[pointer1]
        val2 = l2[pointer2]
        if val1 <= val2:
            result.append(val1)
            pointer1 += 1
        else:
            result.append(val2)
            pointer2 += 1

    return result + l1[pointer1:] + l2[pointer2:]

if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    merged = [1, 1, 2, 3, 4, 4]
    assert merge_two_sorted_lists(list1, list2) == merged
    assert merge_two_sorted_lists([], list1) == list1
    assert merge_two_sorted_lists([], []) == []
