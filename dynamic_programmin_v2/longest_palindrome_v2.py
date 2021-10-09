from pprint import pprint


def lps(s1, s2):
    n = len(s1) + 1
    t = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, n):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    pprint(t)
    i, j = len(s1), len(s1)

    result = ""
    while i > 0 and j > 0:
        if t[i][j] == t[i][j-1]:
            j -= 1
        elif t[i][j] == t[i-1][j]:
            i -= 1
        elif t[i][j] == t[i-1][j-1] + 1:
            result += s1[i-1]
            i -= 1
            j -= 1

    return result


def longest_palindrome_subsequence(s):
    return lps(s, s[::-1])


print(longest_palindrome_subsequence('"aacabdkacaa"'))
