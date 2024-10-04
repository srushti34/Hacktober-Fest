def binary_search(arr, left, right, target:
 if right >= left:
    mid = (left + right) / 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)
 else:
    return -1