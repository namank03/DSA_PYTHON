from functools import lru_cache

ans = ""


def solution(s):
    @lru_cache(maxsize=None)
    def solve(s1, s2):
        global ans
        if len(s1) == 0 or len(s2) == 0:
            return ""
        if s1[-1] == s2[-1]:
            tmp_ans = s1[-1] + solve(s1[:-1], s2[:-1])
            if len(tmp_ans) > len(ans):
                ans = tmp_ans
            return tmp_ans
        solve(s1[:-1], s2)
        solve(s1, s2[:-1])
        return ""

    solve(s, s[::-1])
    return ans


s = "babad"

res = solution(s)
print(f'res -> {res}')
