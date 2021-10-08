def find_union_intersection(arr1, arr2):
    return set(arr1+arr2), set(arr1).intersection(arr2)


print(find_union_intersection([1, 2, 3, 4], [1, 0, 8, 7]))
