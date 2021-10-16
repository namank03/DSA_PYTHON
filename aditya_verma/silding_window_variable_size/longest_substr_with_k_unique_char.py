import snoop


@snoop
def longest_substr_with_k_unique(s, k):
    i = j = 0

    g_r = 0
    c_r = {}

    while j < len(s):

        # Initial Calculations on adding elements from right side
        c_r[s[j]] = c_r.get(s[j], 0) + 1

        # Increasing the window size
        if len(c_r) < k:
            j += 1

        # If the condition is hit update the global result
        elif len(c_r) == k:
            g_r = max(g_r, sum(c_r.values()))
            j += 1

        elif len(c_r) > k:
            # Making window valid again by shrinking the size from the left
            while len(c_r) > k:
                c_r[s[i]] -= 1
                if c_r[s[i]] == 0:
                    del c_r[s[i]]
                i += 1

            # Sliding window further
            j += 1

    return g_r


print(longest_substr_with_k_unique('aabacbebebe', 3))
