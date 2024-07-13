def bubble_sort_str(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if str(arr[j]) > str(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort_str(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and str(key) < str(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort_str(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if str(arr[j]) < str(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort_str(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_str(left_half)
        merge_sort_str(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if str(left_half[i]) < str(right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def heapify_str(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and str(arr[i]) < str(arr[left]):
        largest = left

    if right < n and str(arr[largest]) < str(arr[right]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_str(arr, n, largest)

def heap_sort_str(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify_str(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_str(arr, i, 0)
    return arr

def counting_sort_str(arr):
    arr = list(map(str, arr))
    
    max_val = max(arr, key=str)
    min_val = min(arr, key=str)
    range_of_elements = ord(max_val[0]) - ord(min_val[0]) + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[ord(num[0]) - ord(min_val[0])] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[ord(num[0]) - ord(min_val[0])] - 1] = num
        count[ord(num[0]) - ord(min_val[0])] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
    return arr


def counting_sort_for_radix_str(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 256

    for i in range(n):
        index = ord(str(arr[i])[exp]) if exp < len(str(arr[i])) else 0
        count[index] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = ord(str(arr[i])[exp]) if exp < len(str(arr[i])) else 0
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort_str(arr):
    max_len = max(len(str(x)) for x in arr)
    for exp in reversed(range(max_len)):
        counting_sort_for_radix_str(arr, exp)
    return arr

def partition_str(arr, low, high):
    i = (low - 1)
    pivot = str(arr[high])

    for j in range(low, high):
        if str(arr[j]) <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_str(arr, low, high):
    if low < high:
        pi = partition_str(arr, low, high)
        quick_sort_str(arr, low, pi - 1)
        quick_sort_str(arr, pi + 1, high)
    return arr

def quick_sort_wrapper_str(arr):
    return quick_sort_str(arr, 0, len(arr) - 1)
