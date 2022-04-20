from numpy import sort

arr = [2, 3, 4, 1]
k = 2

# all combinations of size k
def backtrack(result, temp_res, arr, k):
    #  condition if the things are valid if yes then add it in result.
    if len(temp_res) == k:
        result.append(temp_res[:])

    for index, i in enumerate(arr):
        temp_res.append(i)
        backtrack(result, temp_res, arr[index + 1 :], k)
        temp_res.pop()


def main(arr, k):
    result = []
    arr.sort()
    backtrack(result, [], arr, k)
    return result


arr = [1, 10, 2]
res = main(arr, 2)

print(f'res -> {res}')
