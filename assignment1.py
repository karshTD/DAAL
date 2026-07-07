
import random
import time
import string

def generate_username():
    length = random.randint(3, 20)
    chars = string.ascii_lowercase + string.digits + "_."
    
    while True:
        username = ''.join(random.choice(chars) for _ in range(length))
        
        if username[0] in "_." or username[-1] in "_.":
            continue
        if ".." in username or "__" in username or "._" in username or "_." in username:
            continue
        if any(c.isspace() for c in username):
            continue
        return username

def generate_usernames(n):
    usernames = set()
    while len(usernames) < n:
        usernames.add(generate_username())
    return list(usernames)

def linear_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons

def binary_search_recursive(arr, key, low, high, comparisons=0):
    if low > high:
        return -1, comparisons
    
    mid = (low + high) // 2
    comparisons += 1
    
    if arr[mid] == key:
        return mid, comparisons
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, key, low, mid - 1, comparisons)

def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, comparisons

usernames = generate_usernames(50)
sorted_usernames = sorted(usernames)

target = random.choice(usernames)
not_found_target = "nonexistent_user_123"

print("=" * 70)
print("USERNAME SEARCH PERFORMANCE ANALYSIS")
print("=" * 70)
print(f"Total usernames in database: {len(usernames)}")
print(f"Searching for username: '{target}'")
print("=" * 70)

print("\n--- LINEAR SEARCH ---")
start_time = time.time()
index, comparisons = linear_search(usernames, target)
end_time = time.time()
time_taken = (end_time - start_time) * 1000

if index != -1:
    print(f"Found at position: {index}")
else:
    print("Not found")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {time_taken:.6f} ms")

print("\n--- BINARY SEARCH (RECURSIVE) ---")
start_time = time.time()
index, comparisons = binary_search_recursive(sorted_usernames, target, 0, len(sorted_usernames) - 1)
end_time = time.time()
time_taken = (end_time - start_time) * 1000

if index != -1:
    print(f"Found at position: {index}")
else:
    print("Not found")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {time_taken:.6f} ms")

print("\n--- BINARY SEARCH (ITERATIVE) ---")
start_time = time.time()
index, comparisons = binary_search_iterative(sorted_usernames, target)
end_time = time.time()
time_taken = (end_time - start_time) * 1000

if index != -1:
    print(f"Found at position: {index}")
else:
    print("Not found")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {time_taken:.6f} ms")

print("\n" + "=" * 70)
print("SEARCH FOR NON-EXISTENT USERNAME")
print("=" * 70)
print(f"Searching for username: '{not_found_target}'")
print("=" * 70)

print("\n--- LINEAR SEARCH ---")
start_time = time.time()
index, comparisons = linear_search(usernames, not_found_target)
end_time = time.time()
time_taken = (end_time - start_time) * 1000

if index != -1:
    print(f"Found at position: {index}")
else:
    print("Not found")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {time_taken:.6f} ms")

print("\n--- BINARY SEARCH (RECURSIVE) ---")
start_time = time.time()
index, comparisons = binary_search_recursive(sorted_usernames, not_found_target, 0, len(sorted_usernames) - 1)
end_time = time.time()
time_taken = (end_time - start_time) * 1000

if index != -1:
    print(f"Found at position: {index}")
else:
    print("Not found")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {time_taken:.6f} ms")

print("\n--- BINARY SEARCH (ITERATIVE) ---")
start_time = time.time()
index, comparisons = binary_search_iterative(sorted_usernames, not_found_target)
end_time = time.time()
time_taken = (end_time - start_time) * 1000

if index != -1:
    print(f"Found at position: {index}")
else:
    print("Not found")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {time_taken:.6f} ms")

print("\n" + "=" * 70)
print("COMPLEXITY ANALYSIS")
print("=" * 70)
print("Linear Search:")
print("  - Best Case: O(1) - element at first position")
print("  - Worst Case: O(n) - element at last or not present")
print("  - Average Case: O(n)")
print("  - Space Complexity: O(1)")
print()
print("Binary Search (Recursive & Iterative):")
print("  - Best Case: O(1) - element at middle")
print("  - Worst Case: O(log n)")
print("  - Average Case: O(log n)")
print("  - Space Complexity:")
print("    - Iterative: O(1)")
print("    - Recursive: O(log n) due to call stack")
print("=" * 70)
