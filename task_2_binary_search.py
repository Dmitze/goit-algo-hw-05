def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0
    upper = None
    
    while left <= right:
        count += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return (count, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper = arr[mid]
            right = mid - 1
    
    if upper is None and left < len(arr):
        upper = arr[left]
    
    return (count, upper)


nums = [1.5, 2.3, 3.7, 4.2, 5.1, 7.8, 9.5]

print(binary_search(nums, 5.1))
print(binary_search(nums, 4.5))
print(binary_search(nums, 0.5))
print(binary_search(nums, 10.0))
