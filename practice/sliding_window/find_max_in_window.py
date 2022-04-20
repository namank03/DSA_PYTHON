# sliding window fixed size

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 4 find max in window size

# keep i,j
# INIT i = 0, j = 0
# then make the window of required size.
#  if condition is satified then append the window to the result
# else increment j and increment i repeat the process (keep the window size fix)
def find_max_in_window(arr, k):
    #  intitalizing the start and end of the window.
    i = j = 0

    global_res, temp_res = [], []

    # guard condition to prevent window from overflowing
    while j < len(arr):
        # Some Initial Cal here (Cal on the right side of the window).
        temp_res.append(arr[j])
        # Making the window of size k.
        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            #! Some other cal here. (Cal on the left side of the window).
            global_res.append(max(temp_res))
            temp_res.pop(0)

            #! Move the window
            i += 1
            j += 1

    return global_res


arr = [1, 2, 30, 4, 5, 6, 7, 80, 9, 10]

res = find_max_in_window(arr, 3)
print(f'res -> {res}')
