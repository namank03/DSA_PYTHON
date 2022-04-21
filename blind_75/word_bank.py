def word_bank(target, bank, op, memo=None):
    if memo is None:
        memo = {}
    if op == target:
        return True

    if len(op) > len(target):
        return False

    if op in memo:
        return memo[op]

    memo[op] = any(word_bank(target, bank, op + i, memo) for i in bank)
    return memo[op]


print(word_bank("leetcode", ["leet", "code"], ""))
