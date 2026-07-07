def binaryrecursive(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binaryrecursive(arr, key, mid + 1, high)
    else:
        return binaryrecursive(arr, key, low, mid - 1)

arr = [10, 20, 30, 40, 50]
key = 12
result = binaryrecursive(arr, key, 0, len(arr) - 1)
if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the array")

    
