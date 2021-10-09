def longest_common_subsequence(x, y,  n, m):
    if n == 0 or m == 0:
        return 0

    if x[n-1] == y[m-1]:
        return 1 + longest_common_subsequence(x, y, n-1, m-1)
    else:
        return max(longest_common_subsequence(x, y, n - 1, m), longest_common_subsequence(x, y, n, m-1))


x = "mhnan"
y = "mkhan"

print(longest_common_subsequence(x, y, len(x), len(y)))
