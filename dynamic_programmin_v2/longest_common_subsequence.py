from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def lcs(x, y,  n, m):
    if n == 0 or m == 0:
        return 0

    if x[n-1] == y[m-1]:
        return 1 + lcs(x, y, n-1, m-1)
    else:
        return max(lcs(x, y, n - 1, m), lcs(x, y, n, m-1))


x = "mhnan"
y = "mkhan"

print(lcs(x, y, len(x), len(y)))
vs.make_animation("lcs.gif", delay=2)
