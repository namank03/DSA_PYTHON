from functools import lru_cache


def generate_parentheses(n):
    solution = []

    @lru_cache(None)
    def dp(op, o, c):
        if c < o:
            return

        if o < 0 or c < 0:
            return

        if o == 0 and c == 0:
            solution.append(op)
            return

        # o the brackets
        dp(op + "(", o - 1, c)

        dp(op + ")", o, c - 1)

    dp("", n, n)
    return solution


print(generate_parentheses(3))
