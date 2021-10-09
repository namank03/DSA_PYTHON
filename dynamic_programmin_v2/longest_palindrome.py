
# from visualiser.visualiser import Visualiser as vs


# @vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def lp(s1: str, s2: str, memo={}):
    if len(s1) <= 0 or len(s2) <= 0:
        return 0

    if f"{s1},{s2}" in memo:
        return memo[f"{s1},{s2}"]

    if s1[-1] == s2[-1]:
        memo[f"{s1},{s2}"] = 1 + lp(s1[:-1], s2[:-1], memo)
    else:
        memo[f"{s1},{s2}"] = max(lp(s1, s2[:-1], memo), lp(s1[:-1], s2, memo))

    return memo[f"{s1},{s2}"]


s = "namankhan"
print(lp(s, s[::-1]))
# vs.make_animation("lp.gif", delay=2)
