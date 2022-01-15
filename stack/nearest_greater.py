def solve(arr):
    stack = []
    res = []
    for i in arr[::-1]:
        if not stack:
            res.append(-1)
            stack.append(i)
            continue
        while stack and stack[-1] <= i:
            stack.pop()
        res.append(stack[-1]) if stack else res.append(-1)
        stack.append(i)

    return res[::-1]


res = solve([0, 2, 0, 1, 0, 0])
print(f'res -> {res}')


def solve2(arr):
    stack = []
    res = []
    for i in arr[::-1]:
        if not stack:
            res.append(-1)
            stack.append(i)
            continue
        while stack and stack[-1] <= i:
            stack.pop()
        res.append(stack[-1]) if stack else res.append(-1)
        stack.append(i)

    return res


res = solve2([0, 2, 0, 1, 0, 0][::-1])
print(f'res -> {res}')
