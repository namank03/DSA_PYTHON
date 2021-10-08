def sort_array(arr):
    zero_stack = []
    one_stack = []
    two_stack = []

    for i in arr:
        if i == 0:
            zero_stack.append(i)
        elif i == 1:
            one_stack.append(i)
        else:
            two_stack.append(i)

    return zero_stack + one_stack + two_stack


print(sort_array([0, 2, 1, 2, 0]))
