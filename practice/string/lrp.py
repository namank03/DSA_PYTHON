from visualiser.visualiser import Visualiser as vs

s = "aaabaaad"


def lcs(s, t, count):

    if len(s) == 0 or len(t) == 0:
        return count

    if s[-1] == t[-1]:
        count = lcs(s[:-1], t[:-1], count + 1)

    count = max(count, max(lcs(s[:-1], t, 0), lcs(s, t[:-1], 0)))

    return count


res = lcs(s, s[::-1], 0)
print(f'res -> {res}')
