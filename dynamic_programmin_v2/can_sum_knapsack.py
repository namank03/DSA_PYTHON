from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def can_sum(arr, n, target):
    if target == 0:
        return True

    if n == 0:
        return False

    if arr[n-1] <= target:
        return can_sum(arr, n, target - arr[n-1]) + can_sum(arr, n-1, target)
    else:
        return can_sum(arr, n-1, target)


print(can_sum([3, 2, 1], 3, 11))
vs.make_animation('images/can_sum.gif', delay=2)
