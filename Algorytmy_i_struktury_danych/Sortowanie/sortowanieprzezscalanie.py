def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merged_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    left_sorted = merged_sort(left)
    right_sorted = merged_sort(right)

    return merge(left_sorted, right_sorted)


l = [0, 3, 6, 8, 2, 1, 7, 9, 4, 5, 6]
sorted_list = merged_sort(l)
print(sorted_list)