__author__ = 'zhenyuan'

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # There must be a list which is empty
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):

    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)

test_list = [5, 3, 4, 6, 11, 33, 1, 3]
test_listb = [5, 67, 3, 23, 8]
test_list = test_list + test_listb
print(test_list)
sortedList = merge_sort(test_list)
print(sortedList)







