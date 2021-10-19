
def lps(s):
    def dp(s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            return ""

        if s1[-1] == s2[-1]:
            return s1[-1] + dp(s1[:-1], s2[:-1])

        op1 = dp(s1, s2[:-1])
        op2 = dp(s1[:-1], s2)

        if len(op1) > len(op2):
            return op1
        else:
            return op2

    return dp(s, s[::-1])
