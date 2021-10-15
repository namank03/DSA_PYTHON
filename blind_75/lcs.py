def lcs(text1, text2, memo={}):
    if text1 == "" or text2 == "":
        return 0

    comb = text1 + "," + text2
    if comb in memo:
        return memo[comb]

    if text1[-1] == text2[-1]:
        memo[comb] = 1 + lcs(text1[:-1], text2[:-1])
    else:
        memo[comb] = max(lcs(text1[:-1], text2), lcs(text1, text2[:-1]))

    return memo[comb]


print(lcs("abcde", "ace"))
