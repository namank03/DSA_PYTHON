
from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})


# ! the below code is wrong.
def solve(n, m):

    if n < 1 or m < 1:
        return 0

    return 1 + solve(n, m - 1) + solve(n - 1, m)


res = solve(3, 3)
vs.make_animation("images/square.gif", delay=2)
