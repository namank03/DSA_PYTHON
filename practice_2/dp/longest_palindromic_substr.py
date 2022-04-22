def longest_palidromic_substr(s):
    if len(s) < 2:
        return s

    max_len = 0

    def solve(j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        return j + 1, k - j - 1

    for i in range(len(s)):
        start, length = max(solve(i, i), solve(i, i + 1))
        max_len = max(max_len, length)

    return max_len


res2 = longest_palidromic_substr("cxbbxd")
print(f'res -> {res2}')
