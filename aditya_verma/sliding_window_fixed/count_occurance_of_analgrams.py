from collections import Counter


def count_occurrences(s, pat, n, k):

    i = j = 0

    g_r = 0
    c_r = Counter(pat)

    while j < n:
        # Some init cal.
        if s[j] in c_r:
            c_r[s[j]] = c_r.get(s[j]) - 1

        # make window of size k
        if j-i+1 < k:
            j += 1

        elif j-i+1 == k:
            # Do some other cal
            if all(i == 0 for i in c_r.values()):
                print(s[i:j+1])
                g_r += 1

            if s[i] in c_r:
                c_r[s[i]] += 1
            # Remove the ith element from the window cal and then move the window
            i += 1
            j += 1

    return g_r


print(count_occurrences('aabaabaa', 'aaba', 8, 4))
