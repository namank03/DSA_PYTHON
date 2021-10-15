# brute for is to use 3 for loops which will give O(n^3) complexity.
#! Another efficient way is to get the 2 sum and then use hash map to check if there is any 3rd element which can be added to make the result 0
# contraint in the problem is that all 3 values must be diff. so for 1st 2 element we can make sure that they're diff via using for loop and when we find the 3rd element we can then check if this element is equal to 1st and 2nd element.

# * Example algo - 2,1,1 = a,b,c if we're able to identify a,b i.e -2, 1. then 0 = a+b+c => c = 0 - (a+b).

def three_sum_opt(nums):

    d = {val: index for index, val in enumerate(nums)}

    result = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a, b = nums[i], nums[j]
            c = 0 - (a + b)
            if c in d and c not in [a, b]:
                result.add(tuple(sorted([a, b, c])))

    return list(result)


print(three_sum_opt([-1, 0, 1, 2, -1, -4]))
