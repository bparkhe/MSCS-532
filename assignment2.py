import time
import sys

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    sorted_arr.extend(left)
    sorted_arr.extend(right)
    return sorted_arr

# Function to generate test data
def generate_data(size, data_type='random'):
    if data_type == 'random':
        return [random.randint(1, 10000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reverse_sorted':
        return list(range(size, 0, -1))

# Performance Measurement
def measure_performance(sort_function, data):
    start_time = time.time()
    sorted_data = sort_function(data)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Test different datasets
data_sizes = [1000, 5000, 10000]
data_types = ['random', 'sorted', 'reverse_sorted']
results = {}

for data_size in data_sizes:
    results[data_size] = {}
    for data_type in data_types:
        data = generate_data(data_size, data_type)
        quick_sort_time = measure_performance(quick_sort, data.copy())
        merge_sort_time = measure_performance(merge_sort, data.copy())
        
        results[data_size][data_type] = {
            'Quick Sort Time': quick_sort_time,
            'Merge Sort Time': merge_sort_time
        }

# Print results
for size, data_results in results.items():
    print(f"\nData Size: {size}")
    for data_type, times in data_results.items():
        print(f"{data_type.capitalize()} - Quick Sort: {times['Quick Sort Time']:.6f} sec, Merge Sort: {times['Merge Sort Time']:.6f} sec")
