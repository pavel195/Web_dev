import random
def bubbleSort(array):
    l = len(array)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

def choice(array): #o(n2)
    l = len(array)
    for i in range(l-1):
        m = array[i]          # идем с лева на право от 0 элемента до конца
        id = i        # запоминаем индекс "минимального числа"
        for j in range(i+1,l):
            if m > array[j]:     # есть число меньше
                m = array[j]       # запоминаем его и его индекс
                id = j
        if id!=i:           # меняем их местами
            array[i],array[id] = array[id],array[i]
    return array

def insertion(lst):
    for i in range(1, len(lst)):
        xi = lst[i]
        i2 = i - 1
        while i2 >= 0 and lst[i2] > xi:
            lst[i2 + 1] = lst[i2]
            i2 -= 1
        lst[i2 + 1] = xi
def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_insertion_sort(lst):
    for i in range(1, len(lst)):
        val = lst[i]
        j = binary_search(lst, val, 0, i - 1)
        lst = lst[:j] + [val] + lst[j:i] + lst[i + 1:]
    return lst

def q_sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return q_sort(less)+equal+q_sort(greater)
    else:
        return array
if __name__ == '__main__':

    array = [random.randint(1,100) for x in range(10)]
    print(array)
    print(q_sort(array))
    print(binary_insertion_sort(array))