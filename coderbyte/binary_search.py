def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
    return 0

nums = [2,7,8,9,10,13,17,19,21]
print(binary_search(nums, 7))
print(binary_search(nums, 15))
