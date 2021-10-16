import math

# IP = [2, 5, 8, 2, 9, 1], size = 7 window_size(k) = 3
# OP= Find max of subarray of size k.

#! fixed size window ques Identification ->
# 1. arr or str
# 2. subarray or substr
# 3. window size or condition

#  All the above identification is matching so we can think about applying the sliding window here.

# * Approach -
# We need something to represent the start and the end of the window. We'll use i,j. Window size(k) is always "j-i+1".
# we need to 1st keep both i,j at start and then we need to move j till it reaches the window size i.e j-i+1. When the window size is reached then we need to maintain the window size.
# When the window size is reached then we need to perform some required calculation while keeping the window size fixed.


def sliding_window_template(arr, n, k):
    #  intitalizing the start and end of the window.
    i = j = 0

    # This variable will store the result. Initialize the result variable
    global_result = -math.inf
    current_window_result = 0
    # guard condition to prevent window from overflowing
    while j < n:
        # Some Initial Cal here.

        # Making the window of size k.
        if j-i + 1 < k:
            j += 1

        # Now the window is formed and we can do 2 things.
        elif j-i+1 == k:
            #! Some other cal here
            #! Move the window
            i += 1
            j += 1

    return global_result


print(sliding_window_template([2, 5, 8, 2, 9, 1, 3], 7, 3))
