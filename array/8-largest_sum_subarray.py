def largest_sum_subarray(arr):
    # Current sum will keep track to of the running sum and will be used to evaluate the start index
    current_sum = 0
    #  max sum will be used to keep track of end index
    max_sum = 0
    end_index = 0
    start_index = 0

    # ! Here the idea is to iterate over the array and keep track of current sum if at any point of time current sum  goes < 0 then we discard that slice as it'll not gonna contribute in max sum. Then we also keep track of end index via keeping track of max sum
    for index, i in enumerate(arr):
        current_sum += i
        # Index + 1 < len(arr) will manage the edge case.
        if current_sum < 0 and index + 1 < len(arr):
            start_index = index + 1
            current_sum = 0
            max_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
            end_index = index + 1

    return arr[start_index:end_index]


print(largest_sum_subarray([20, -300, 10, 4, 3, 60]))
