def cyclic_rotate(arr, right=False):
    return [arr[-1]] + arr[:-1] if right else arr[1:] + [arr[0]]


print(cyclic_rotate([9, 0, 2, 1, 2], right=True))
