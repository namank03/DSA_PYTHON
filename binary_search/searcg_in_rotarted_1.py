def search(arr, target):
    low, high = 0, len(arr) -1
    if not arr:
        return -1
    while low <= high:
        mid = (low+high) //2
        if arr[mid] == target:
            return mid
        # left side is sorted
        if arr[low] <= arr[mid]:
            # target is in the left side
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            # target is in the right side
            else:
                low = mid + 1
        else:
            # target is in the right side
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            # target is in the left side
            else:
                high = mid - 1
    return -1



def search_with_repetation(arr, target):
    low, high = 0, len(arr) -1
    if not arr:
        return -1
    while low <= high:
        mid = (low+high) //2
        if arr[mid] == target:
            return mid
        while low < mid and arr[low] == arr[mid]:
            low += 1
        # left side is sorted
        if arr[low] <= arr[mid]:
            # target is in the left side
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            # target is in the right side
            else:
                low = mid + 1
        else:
            # target is in the right side
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            # target is in the left side
            else:
                high = mid - 1
    return -1
    
