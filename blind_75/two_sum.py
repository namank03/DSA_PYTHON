def two_sum(arr, target):
    # ! Trick is to use the dictionary and insert the difference as the key and index as the value.
    d = {}
    for index, value in enumerate(arr):
        if value in d:
            return [d[value], index]
        d[value] = index
