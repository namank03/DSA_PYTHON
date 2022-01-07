def longestConsecutive(nums) -> int:
    # create hash set
    hash_set = set(nums)
    max_len = 0
    for i in nums:
        #  checking if this is the smallest number
        if i - 1 not in hash_set:
            count = 0
            while i in hash_set:
                count += 1
                i += 1
            max_len = max(max_len, count)
    return max_len
