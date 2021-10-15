# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4

def lcs(arr, n):

    if n < 2:
        return 1

    if arr[n-1] > arr[n-2]:
        return max(1 + lcs(arr, n-1), lcs(arr, n-1))
    else:
        return lcs(arr, n-1)


print(lcs([1, 10, 4, 3, 7], 5))
