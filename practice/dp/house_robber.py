# [10,10,1,100,12]
# can't loot alterante items

from visualiser.visualiser import Visualiser as vs


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "grey",
    }
)
def solve(arr):
    return max(arr[0] + solve(arr[2:]), solve(arr[1:])) if arr else 0


res = solve([10, 10, 1, 100, 12])
vs.make_animation("images/path.gif", delay=2)
print(f'res -> {res}')
