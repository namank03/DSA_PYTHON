def partition(s):
    res = []
    dfs(s, [], res)
    return res


def dfs(s, path, res):
    if not s:
        res.append(path)
    for i in range(1, len(s) + 1):
        if isPalindrome1(s[:i]):
            dfs(s[i:], path + [s[:i]], res)


def isPalindrome1(s):
    return s == s[::-1]


res = partition('aaba')
print(f'res -> {res}')
