def word_bank(s, wordDict, memo={}):
    if s == "":
        return True

    if s in memo:
        return memo[s]

    for i in wordDict:
        if s.startswith(i) and word_bank(s[len(i):], wordDict, memo):
            memo[s] = True
            return True

    memo[s] = False
    return False
