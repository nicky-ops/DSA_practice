def binary_search(arr, target):
    '''
    This function searches for the target element in list arr, using the binary search algorithm
    Args:
        - arr(list): list of elements to be searched
        - target(int): element to look for in the list
    Return:
        - index(int): position of the element in the sorted list/array
    '''
    end = len(arr) - 1
    start = 0
    sorted_arr = sorted(arr)
    print(sorted_arr)

    while start <= end:
        mid = start + (end - start) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(binary_search([2, 4, 1, 89, 43, 12, 789, 13, 67, 15], 13))
