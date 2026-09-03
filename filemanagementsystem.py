def merge_sort(arr):
    print(f"split files: {arr}")
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right= merge_sort(arr[:mid])

    result = merge(left, right)
