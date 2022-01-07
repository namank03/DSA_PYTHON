import math


def functionName(arr, windowSize):
    #  intitalizing the start and end of the window.
    i = j = 0

    # This the current window result and the global/final result
    global_result = 0
    current_window_result = 0

    # guard condition to prevent window from overflowing
    while j < len(arr):
        # Some Initial Cal here (Cal on the right side of the window).

        # Making the window of size k.
        if j - i + 1 < windowSize:
            j += 1

        elif j - i + 1 == windowSize:
            #! Some other cal here. (Cal on the left side of the window).

            #! Move the window
            i += 1
            j += 1

    return global_result


def functionName(arr, target):
    # Initialize the start and end.
    i = j = 0

    # Initialize the running target and mix/min with the required values
    running_target = 0
    max_min_window_size = 0

    while j < len(arr):
        # Doing normal calculations as we used to do earlier in fixed window size.

        # increasing window size. The below condtion can be replaced with the required cond to move the window
        if running_target < target:
            j += 1

        # if the condition is hit then we do our calculations and save the window size.
        elif running_target == target:

            j += 1

        # else we move i till the running sum becomes valid again.
        elif running_target > target:
            while running_target > target:
                # Some cal on i to make window valid

                i += 1

            # Guard condition
            if running_target == target:
                # Some guard cond to remove current j calculations

                continue

            # # Alternative to above guard condition to check the potential answer while shrinking the window size.
            # if running_sum == target_sum:
            #     print(arr[i:j+1])
            #     max_window_size = max(j-i+1, max_window_size)

            j += 1

    return max_min_window_size
