from functools import lru_cache

from visualiser.visualiser import Visualiser as vs


def superEggDrop(k: int, n: int):
    @vs(
        node_properties_kwargs={
            "shape": "record",
            "color": "#f57542",
            "style": "filled",
            "fillcolor": "grey",
        }
    )
    def solve(k, n):
        if n in [0, 1]:
            return n

        if k == 1:
            return n

        return 1 + min(
            max(solve(k - 1, i - 1), solve(k, n - i)) for i in range(1, n + 1)
        )

    return solve(k, n)


res = superEggDrop(2, 3)
print(f'res -> {res}')
vs.make_animation("images/egg_drop.gif", delay=2)
