def cansum(target, num_arr):
    if target < 0:
        return False

    if target == 0:
        return True

    for i in num_arr:
        return cansum(target - i, num_arr)


result = cansum(7, [2, 4])
print(result)
