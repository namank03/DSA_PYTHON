# 39 -> ans [10,10,20]
# 31 -> ans [2, 32]
from ast import Return

arr = [10, 10, 20, 1, 1, 2, 2, 30]


def min_subarr_greater_than_target(arr, target):
    global_res = []
    i, j, running_sum = 0, 0, 0
    while j < len(arr):
        running_sum += arr[j]

        if running_sum >= target:
            while running_sum >= target:
                window_size = j - i + 1
                if window_size < len(global_res) or len(global_res) == 0:
                    global_res = arr[i : j + 1]
                running_sum -= arr[i]
                i += 1
        j += 1
    return global_res


res = min_subarr_greater_than_target(arr, 39)
print(f'res -> {res}')
res = min_subarr_greater_than_target(arr, 31)
print(f'res -> {res}')


# max substr without repeating char

s = "arrnamankp"
# ANS - mankp


def max_substr_without_repeating_char(s):
    global_res = ""
    i, j = 0, 0

    char_map = {}

    while j < len(s):
        # keeping char map
        if s[j] in char_map:
            char_map[s[j]] += 1
        else:
            char_map[s[j]] = 1

        #  result conditon
        if j - i + 1 == len(char_map) and len(global_res) < len(char_map):
            global_res = s[i : j + 1]
        while j - i + 1 > len(char_map):
            char_map[s[i]] -= 1
            if char_map[s[i]] == 0:
                del char_map[s[i]]
            i += 1
            if j - i + 1 == len(char_map) and len(global_res) < len(char_map):
                global_res = s[i : j + 1]

        j += 1
    return global_res


res = max_substr_without_repeating_char(s)
print(f'res -> {res}')
