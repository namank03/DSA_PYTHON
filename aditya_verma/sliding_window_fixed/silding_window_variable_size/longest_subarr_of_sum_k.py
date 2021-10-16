
def longest_subarr_of_given_sum(arr, target_sum):
    i = j = 0

    running_sum = 0
    max_window_size = 0
    while j < len(arr):
        # Doing normal calculations as we used to do earlier in fixed window size.
        running_sum += arr[j]

        # increasing window size. pass will not fo through other else-if condition and will just inc j by 1.
        if running_sum < target_sum:
            j += 1

        # if the condition is hit then we do our calculations and save the window size.
        elif running_sum == target_sum:
            print(arr[i:j+1])
            max_window_size = max(j-i+1, max_window_size)
            j += 1

        # else we move i till the running sum becomes valid again.
        elif running_sum > target_sum:

            while running_sum > target_sum:
                running_sum -= arr[i]
                i += 1

            # Guard condition
            if running_sum == target_sum:
                running_sum -= arr[j]
                continue

            j += 1

    return max_window_size


print(longest_subarr_of_given_sum([4, 1, 1, 1, 2, 3, 5], 5))
