__author__ = 'zhenyuan'

def quick_sort(lists, left, right):

    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

test = [4, 5, 8, 1, 9, 2]
result = quick_sort(test, 0, len(test)-1)
print(result)



def quick_sort_standord(array,low,high):
    if low < high:
        key_index = partition2(array, low, high)
        quick_sort_standord(array, low, key_index)
        quick_sort_standord(array, key_index+1, high)

def partition(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low

def partition2(array, low, high):
    i = low + 1
    j = high
    privot_key = array[low]
    while True:
        while array[i] < privot_key:
            i += 1
            if i == high + 1:
                break

        while array[j] > privot_key:
            j -= 1
            if j == low - 1:
                break
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
    array[low], array[j] = array[j], array[low]
    return j



test2 = [5, 4, 1, 22, 6, 8, 2, 44, 7]
print(test2)
quick_sort_standord(test2, 0, len(test2)-1)
print(test2)

