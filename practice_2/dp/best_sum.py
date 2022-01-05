a = [2, 3, 5]
target = 8
from functools import lru_cache


def can_sum(a, target):
    def solve(target):
        if target == 0:
            return []
        if target < 0:
            return None

        best_res = None
        for i in a:
            tmp_res = solve(target - i)
            if tmp_res is not None:
                tmp_res += [i]
                if best_res is None or len(tmp_res) < len(best_res):
                    best_res = tmp_res
        return best_res

    return solve(target)


res = can_sum(a, target)
print(f'res -> {res}')
