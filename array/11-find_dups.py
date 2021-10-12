from collections import Counter


def findDuplicate(nums):
    d = []
    for i in nums:
        if i in d:
            return i
        d.append(i)
