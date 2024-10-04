def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10
    try:
        index = binary_search(arr, target, 0, len(arr) - 1)  
        if index == -1:
            raise ValueError("Target not found in the array")
        print(f"Target found at index: {index}")
    except ValueError as e:
        print(f"ValueError: {e}")

main()
