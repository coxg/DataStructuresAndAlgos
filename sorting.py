import heapq

def merge_sort(data):

    if len(data) <= 1:
        return data

    middle_index = len(data) // 2
    first_half = data[:middle_index]
    second_half = data[middle_index:]
    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)
    return _merge_sorted(sorted_first_half, sorted_second_half)


def _merge_sorted(first_half, second_half):
    first_index = 0
    second_index = 0
    result = []

    while first_index < len(first_half) and second_index < len(second_half):
        first_value = first_half[first_index]
        second_value = second_half[second_index]
        if first_value <= second_value:
            result.append(first_value)
            first_index += 1
        else:
            result.append(second_value)
            second_index += 1

    result += first_half[first_index:]
    result += second_half[second_index:]

    return result


def quicksort(data):

    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]
    smaller_values = []
    larger_values = []
    equal_values = []

    for elem in data:
        if elem == pivot:
            equal_values.append(elem)
        elif elem < pivot:
            smaller_values.append(elem)
        else:
            larger_values.append(elem)

    return quicksort(smaller_values) + equal_values + quicksort(larger_values)


def heapsort(data):
    data_copy = [datum for datum in data]
    heapq.heapify(data_copy)
    result = []
    while data_copy:
        result.append(heapq.heappop(data_copy))
    return result


if __name__ == "__main__":
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert heapsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
