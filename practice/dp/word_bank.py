def word_bank(s, sl):

    if not s:
        return True
    if not sl:
        return False

    return next((word_bank(s[len(i) :], sl) for i in sl if s.startswith(i)), False)


res = word_bank('leetcode', ['leet', 'leet', 'de', 'coe', 'coe', 'ca'])
print(f'tes -> {res}')


# best sum

# a = [1, 2, 3, 4, 5]
# target = 5

# Can you element again? - No


def best_sum(arr, target):

    if target == 0:
        return []

    if not arr or target < 0:
        return None

    op = None

    for i in arr:
        # allowing same number to be used again / if conditon for early  return
        temp_res = best_sum(arr, target - i)
        if temp_res is not None:
            temp_res.append(i)
            if op is None or len(temp_res) < len(op):
                op = temp_res

    return op


res = best_sum([10, 7, 2, 1, 9, 3], 5)
print(f'res -> {res}')

# all sum use backtrack bro


def backtrack(result, tmp_res, arr, target):
    if target == 0:
        result.append(tmp_res[:])
    if target < 0:
        return
    for i in range(len(arr)):
        # avoiding duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        tmp_res.append(arr[i])
        backtrack(result, tmp_res, arr, target - arr[i])
        tmp_res.pop()


def main(arr, target):
    arr.sort()
    result = []
    backtrack(result, [], arr, target)
    return result


res = main([10, 7, 2, 1, 9, 3], 5)
print(f'All res -> {res}')


# kadanes algo
# besttime to buy/sell

# arr = [10, 2, 1, 9, 3]
# max - profit -> 8


def max_profit(arr):

    if not arr:
        return 0

    buy_price, cur_profit, max_profit = arr[0], 0, 0
    for i in arr[1:]:
        cur_profit = i - buy_price
        buy_price = min(buy_price, i)
        max_profit = max(max_profit, cur_profit)

    return max_profit


res = max_profit([100, 50, 2, 1, 9, 30, 300])
print(f'Profit res -> {res}')
