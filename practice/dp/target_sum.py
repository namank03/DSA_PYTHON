from visualiser.visualiser import Visualiser as vs

a = [2, 23, 1, 5]
t = 8


def target_sum(a, t):

    @vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
    def solve(n, t):

        if t == 0:
            return True

        if n == 0 or t < 0:
            return False

        if a[n-1] <= t:
            return solve(n-1, t - a[n-1]) or solve(n-1, t)
        else:
            return solve(n-1, t)

    return solve(len(a), t)


res = target_sum(a, t)
print(f'res -> {res}')
vs.make_animation("images/target_sum.gif", delay=2)
