def test(arr):
    arr.sort()
    i, j = 0, len(arr) - 1
    count = 0
    while i < j:
        if (arr[i] + arr[j]) % 60 == 0:
            count += 1
        if (arr[i + 1] + arr[j]) % 60 == 0:
            count += 1
        if (arr[i] + arr[j - 1]) % 60 == 0:
            count += 1
        i += 1
        j -= 1
    return count


arr = [30, 90, 60, 20, 30]
res = test(arr)
print(f'res -> {res}')
