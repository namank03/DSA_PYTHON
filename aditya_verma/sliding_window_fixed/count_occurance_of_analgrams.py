from collections import Counter


def count_occurrences(s, pat, n, k):

    i = j = 0

    g_r = 0
    c_r = Counter(pat)

    # initialize the count with the counter size
    count = len(c_r)

    while j < n:
        # Some init cal.
        if s[j] in c_r:
            c_r[s[j]] -= 1

            # if char count goes to 0 then we need to decrease the total variable count
            if c_r[s[j]] == 0:
                count -= 1

        # make window of size k
        if j-i+1 < k:
            j += 1

        elif j-i+1 == k:
            # Do some other cal
            # When there's no element in the counter/map the count will go to 0
            if count == 0:
                print(s[i:j+1])
                g_r += 1

            #  as we move forward we need to inc the count of the element at postition i if it's decreased before.
            if s[i] in c_r:
                c_r[s[i]] += 1

            #  we inc the variable count only once and if there's a duplicate element the if condition will be ignored.
            if c_r[s[i]] == 1:
                count += 1
            # Remove the ith element from the window cal and then move the window
            i += 1
            j += 1

    return g_r


print(count_occurrences('aabanabaa', 'aaba', 9, 4))
