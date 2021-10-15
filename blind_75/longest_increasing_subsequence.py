# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
#  We've got 2 variables to track i,j element at i will hold the current element and the element at j will hold the another element. This way we can compare the 2. So, we need 2 variable for this.

# Now to think of a bc think of a smallest input and that'll be a empty array and it'll retrun 0. And if there's just 1 element in an array it's lcs is 1.

def lcs(arr, n):

    if n < 2:
        return 1

    if arr[n-1] > arr[n-2]:
        return max(1 + lcs(arr, n-1), lcs(arr, n-1))
    else:
        return lcs(arr, n-1)


print(lcs([1, 10, 4, 3, 7], 5))
