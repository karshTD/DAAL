import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    swaps = 0
    
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    
    return i + 1, comparisons, swaps

def quick_sort(arr, low, high):
    comparisons = 0
    swaps = 0
    
    if low < high:
        pi, comp, swp = partition(arr, low, high)
        comparisons += comp
        swaps += swp
        
        comp_left, swp_left = quick_sort(arr, low, pi - 1)
        comp_right, swp_right = quick_sort(arr, pi + 1, high)
        
        comparisons += comp_left + comp_right
        swaps += swp_left + swp_right
    
    return comparisons, swaps

def analyze_quick_sort(input_type, size=1000):
    if input_type == "random":
        arr = [random.randint(1, 10000) for _ in range(size)]
    elif input_type == "sorted":
        arr = list(range(1, size + 1))
    elif input_type == "reverse":
        arr = list(range(size, 0, -1))
    
    arr_copy = arr.copy()
    
    start_time = time.time()
    comparisons, swaps = quick_sort(arr_copy, 0, len(arr_copy) - 1)
    end_time = time.time()
    
    return {
        'input_type': input_type,
        'time': end_time - start_time,
        'comparisons': comparisons,
        'swaps': swaps,
        'first_5_original': arr[:5],
        'first_5_sorted': arr_copy[:5]
    }

def main():
    print("Quick Sort Performance Analysis")
    print("Input Size: 1000 elements\n")
    print("-" * 60)
    
    results = []
    
    for input_type in ["random", "sorted", "reverse"]:
        result = analyze_quick_sort(input_type)
        results.append(result)
        
        print(f"\nInput: {input_type.upper()}")
        print(f"  Time:        {result['time']:.6f} seconds")
        print(f"  Comparisons: {result['comparisons']:,}")
        print(f"  Swaps:       {result['swaps']:,}")
        print(f"  First 5 (original): {result['first_5_original']}")
        print(f"  First 5 (sorted):   {result['first_5_sorted']}")
    
    print("\n" + "-" * 60)
    print("\nSummary:")
    
    fastest = min(results, key=lambda x: x['time'])
    slowest = max(results, key=lambda x: x['time'])
    
    print(f"  Fastest:  {fastest['input_type'].upper()} - {fastest['time']:.6f}s")
    print(f"  Slowest:  {slowest['input_type'].upper()} - {slowest['time']:.6f}s")
    
    if fastest['time'] > 0:
        ratio = slowest['time'] / fastest['time']
        print(f"  Slowest is {ratio:.2f}x slower than fastest")
    
    print("\nKey Observations:")
    print("  1. Random input gives best performance (balanced partitions)")
    print("  2. Sorted input gives worst performance (pivot always maximum)")
    print("  3. Reverse input gives worst performance (pivot always minimum)")
    print("  4. Input order significantly affects Quick Sort efficiency")

if __name__ == "__main__":
    main()