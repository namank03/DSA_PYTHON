import sys
from functools import lru_cache

count = 0
solution = None


@lru_cache(maxsize=None)
def solve(ip, op, k):
    global count

    if ip == "":
        if count == k - 1:
            print(op)
            sys.exit()
        count += 1
        return

    for index, i in enumerate(ip):
        solve(ip[:index] + ip[index+1:], op + i, k)

    return


def kth_permutation(n, k):
    ip = "".join(str(i) for i in range(1, n+1))
    op = ""
    solve(ip, op, k)


kth_permutation(10, 3434989)
