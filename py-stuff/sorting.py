def bubbleSort(array):
    l = len(array)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array


def insertion(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while array[j] > x and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x
    return array


def insertion_binary(array):
    for i in range(len(array)):
        key = array[i]
        start, end = 0, i - 1
        while start < end:
            mid = start + (end - start) // 2
            if key < array[mid]:
                end = mid
            else:
                start = mid + 1
        for j in range(i, start + 1, -1):
            array[j] = array[j - 1]
        array[start] = key
    return array


print(bubbleSort([3, 21, 10]))
