def binary_search(l: list[int], v: int) -> int:
    left = 0
    right = len(l) - 1
    while left <= right:
        center = (left + right) // 2
        if l[center] < v:
            left = center + 1
        elif l[center] > v:
            right = center - 1
        else:
            return center
    return -1


if __name__ == "__main__":
    assert binary_search(list(range(1000)), 0) == 0
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
