def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  
    return -1 


arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)
print("Found at index:", result)  





def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [10, 20, 30, 40, 50]  
target = 40
result = binary_search(arr, target)
print("Found at index:", result)  
