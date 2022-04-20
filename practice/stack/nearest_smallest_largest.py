# next smallest to left
def solve_next_smallest_to_left(arr):
    stack, res = [], []
    for index, val in enumerate(arr):
        if not stack:
            res.append(-1)
        elif stack[-1][0] < val:
            res.append(stack[-1][0])
        else:
            while stack and stack[-1][0] >= val:
                stack.pop()
            res.append(stack[-1][0]) if stack else res.append(-1)
        stack.append((val, index))
    return res


arr = [1, 5, 3, 2, 10, 8]

k = solve_next_smallest_to_left(arr)
print(f'next_smallest_to_left -> {k}')


# next smallest to right
def solve_next_smallest_to_right(arr):
    stack, res = [], []
    for index, val in enumerate(arr):
        if not stack:
            res.append(-1)
        elif stack[-1][0] < val:
            res.append(stack[-1][0])
        else:
            while stack and stack[-1][0] >= val:
                stack.pop()
            res.append(stack[-1][0]) if stack else res.append(-1)
        stack.append((val, index))
    return res[::-1]


arr = [1, 5, 3, 2, 10, 8]

k = solve_next_smallest_to_right(arr[::-1])
print(f'next_smallest_to_right -> {k}')


# next greatest to right
def solve_next_greatest_to_right(arr):
    stack, res = [], []
    for index, val in enumerate(arr):
        if not stack:
            res.append(-1)
        elif stack[-1][0] > val:
            res.append(stack[-1][0])
        else:
            while stack and stack[-1][0] <= val:
                stack.pop()
            res.append(stack[-1][0]) if stack else res.append(-1)
        stack.append((val, index))
    return res[::-1]


arr = [1, 5, 3, 2, 10, 8]

k = solve_next_greatest_to_right(arr[::-1])
print(f'next_smallest_to_right -> {k}')


# next greatest to left
def solve_next_greatest_to_left(arr):
    stack, res = [], []
    for index, val in enumerate(arr):
        if not stack:
            res.append(-1)
        elif stack[-1][0] > val:
            res.append(stack[-1][0])
        else:
            while stack and stack[-1][0] <= val:
                stack.pop()
            res.append(stack[-1][0]) if stack else res.append(-1)
        stack.append((val, index))
    return res


arr = [1, 5, 3, 2, 10, 8]

k = solve_next_greatest_to_left(arr)
print(f'next_smallest_to_left -> {k}')


# Tempalte
# def solve_next_smallest_to_left(arr):
#     # initialize stack / res
#     stack, res = [], []
#     for index, val in enumerate(arr):
#         # init egde, when there's nothing on stack
#         if not stack:
#             res.append(-1)
#         # comparison step used for greatest / smallest
#         elif stack[-1][0] < val:
#             res.append(stack[-1][0])
#         else:
#             # stack pop & comparison step
#             while stack and stack[-1][0] >= val:
#                 stack.pop()
#             res.append(stack[-1][0]) if stack else res.append(-1)
#         # add element in stack after processing
#         stack.append((val, index))
#     # retrun result or result[::-1] to control left / right
#     return res
