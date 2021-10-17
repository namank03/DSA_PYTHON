
def number_of_subarr(arr, k, threshold):
    #  intitalizing the start and end of the window.
    i = j = 0

    # This the current window result and the global/final result
    global_result = 0
    current_avg = 0

    # guard condition to prevent window from overflowing
    while j < len(arr):
        # Some Initial Cal here (Cal on the right side of the window).
        current_avg += arr[j] / k

        # Making the window of size k.
        if j-i + 1 < k:
            j += 1

        elif j-i+1 == k:
            #! Some other cal here. (Cal on the left side of the window).
            if current_avg >= threshold:
                global_result += 1

            current_avg -= arr[i] / k
            #! Move the window
            i += 1
            j += 1

    return global_result
