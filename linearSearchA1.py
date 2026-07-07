def linearsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1  


arr = [10, 20, 30, 40, 50]
key = 30
result = linearsearch(arr, key)
if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the array")

