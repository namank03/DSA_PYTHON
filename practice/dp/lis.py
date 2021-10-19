from visualiser.visualiser import Visualiser as vs

nums = [10, 9, 21, 5, 3, 101, 18]


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def dp(pos: int) -> int:
    max_length = 1  # We have 1-element subsequence anyway

    for next_pos in range(pos + 1, len(nums)):
        print(f'nums[next_pos] -> {nums[next_pos]}')
        if nums[pos] < nums[next_pos]:
            max_length = max(max_length, dp(next_pos) + 1)

    return max_length


dp(0)
vs.make_animation("images/lis.gif", delay=2)
