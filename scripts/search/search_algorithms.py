def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search_all(arr, target):
    left, right = 0, len(arr) - 1
    result = []
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result.append(mid)
            # Buscar a la izquierda
            l, r = mid - 1, mid + 1
            while l >= 0 and arr[l] == target:
                result.append(l)
                l -= 1
            # Buscar a la derecha
            while r < len(arr) and arr[r] == target:
                result.append(r)
                r += 1
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return sorted(result)

def linear_search_all(arr, target):
    return [index for index, value in enumerate(arr) if value == target]
