
from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def cansum(target, num_arr):
    if target < 0:
        return False

    if target == 0:
        return True

    for i in num_arr:
        return cansum(target - i, num_arr)


result = cansum(7, [2, 4])
print(result)
vs.make_animation("images/can_sun.gif", delay=2)
