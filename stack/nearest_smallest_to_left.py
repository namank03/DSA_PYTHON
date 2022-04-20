def solve(arr):
    res = []
    stack = []
    for index, val in enumerate(arr):
        # cond if not stack. Initialize res here for edges
        if not stack:
            res.append(-1)
        elif stack[-1][0] < val:
            res.append(stack[-1][-1])
        else:
            while stack and stack[-1][0] >= val:
                stack.pop()
            # Two scenarios can happen here
            res.append(stack[-1][-1]) if stack else res.append(-1)
        stack.append((val, index))

    return res


arr = [1, 7, 6, 8, 5]

res = solve(arr)
print(f'res -> {res}')
