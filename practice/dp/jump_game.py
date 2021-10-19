
from visualiser.visualiser import Visualiser as vs


def jump_game(nums):
    @vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
    def dp(start):
        if start >= len(nums) - 1:
            return 0

        min_len = 90
        for i in range(nums[start] + 1):
            if i != 0:
                result = 1 + dp(start + i)
                if result is not None and result < min_len:
                    min_len = result

        return min_len

    return dp(0)


nums = [2, 3, 1, 1, 4]
print(jump_game(nums))
vs.make_animation("images/jum_game.gif", delay=2)
