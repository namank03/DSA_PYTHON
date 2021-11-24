import queue


def gen_parenthesis(n):
    def solve(o, c, op=""):
        if o == 0 and c == 0:
            print(f'op -> {op}')

        if o < 0 or c < 0 or c < o:
            return

        solve(o-1, c, op+'(')
        solve(o, c-1, op+')')

    solve(n, n)


gen_parenthesis(3)
