from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0

    if x[-1] == y[-1]:
        return 1 + lcs(x[:-1], y[:-1])
    else:
        return max(lcs(x[:-1], y), lcs(x, y[:-1]))


x = "mhnan"
y = "mkhan"

print(lcs(x, y))
vs.make_animation("lcs.gif", delay=2)
