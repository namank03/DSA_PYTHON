#  here the trick is - when there's all unique characters, then the size of the result is equal to the window size.
def longest_substr_without_repeating_char(s):
    i = j = 0

    g_r = 0
    c_r = {}

    while j < len(s):

        # Initial Calculations on adding elements from right side
        c_r[s[j]] = c_r.get(s[j], 0) + 1

        # * Increasing the window size - This 1st if condition is useless here as this condition will never hit map size can't be greater than the window size which is used to create that particular map. So, we can avoid the 1st if condition
        # if len(c_r) > j-i+1:
        # j += 1

        # If the condition is hit update the global result
        if len(c_r) == j-i+1:
            g_r = max(g_r, sum(c_r.values()))
            j += 1

        elif len(c_r) < j-i+1:
            # Making window valid again by shrinking the size from the left
            while len(c_r) < j-i+1:
                c_r[s[i]] -= 1
                if c_r[s[i]] == 0:
                    del c_r[s[i]]
                i += 1

            # Sliding window further
            j += 1

    return g_r


print(longest_substr_without_repeating_char('aabacbebebe'))
