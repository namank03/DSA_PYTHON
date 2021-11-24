def finding_first_negative(arr, n, k):
    #  intitalizing the start and end of the window.
    i = j = 0

    global_result = []
    current_window_result = []
    # guard condition to prevent window from overflowing
    while j < n:
        # Initial base calculations
        if arr[j] < 0:
            current_window_result.append(arr[j])

        # Making the window of size k. And at the same time we're evaluating the sum
        if j-i+1 < k:
            j += 1

        elif j-i+1 == k:
            if not current_window_result:
                global_result.append(0)
            else:
                global_result.append(current_window_result[0])
            if arr[i] < 0:
                current_window_result.pop(0)

            i += 1
            j += 1

    return global_result


print(finding_first_negative([2, 5, -3, 2, 9, 1, 3], 7, 2))
