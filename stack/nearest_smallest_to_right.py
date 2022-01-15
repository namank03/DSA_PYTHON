def solve(arr):
    stack = []
    res = []

    for i in arr[::-1]:
        if not stack:
            res.append(-1)
        elif stack[-1] < i:
            res.append(stack[-1])
        else:
            while stack and stack[-1] >= i:
                stack.pop()
            res.append(-1) if not stack else res.append(stack[-1])
        stack.append(i)
    return res[::-1]


arr = [1, 3, 1, 4, 2, 1, 2, 4, 5]
res = solve(arr)

print(f'res -> {res}')
