
def longest_subarr_of_one(nums):
    # Initialize the start and end.
    i = j = 0

    # Initialize the running target and mix/min with the required values
    max_window_size = -99
    _map = {}

    while j < len(nums):
        # Doing normal calculations as we used to do earlier in fixed window size.
        _map[nums[j]] = _map.get(nums[j], 0) + 1

        # increasing window size. The below condition can be replaced with the required cond to move the window
        if _map.get(0, 0) < 1:
            j += 1

        # if the condition is hit then we do our calculations and save the window size.
        elif _map[0] == 1:
            print(nums[i:j+1])
            max_window_size = max(max_window_size, j-i)
            j += 1

        # else we move i till the running sum becomes valid again.
        elif _map[0] > 1:
            while _map[0] > 1:
                # Some cal on i to make window valid
                _map[nums[j]] -= 1
                i += 1

                # Alternative to above guard condition to check the potential answer while shrinking the window size.
                if _map[0] == 1:
                    print(nums[i:j+1])
                    max_window_size = max(max_window_size, j-i)

            j += 1

    return max_window_size


longest_subarr_of_one([0, 1, 1, 1, 0, 1, 1, 0, 1])
