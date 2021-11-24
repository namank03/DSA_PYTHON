from collections import Counter


def count_occurrences(s, words):

    i = j = 0

    g_r = []
    c_r = Counter(words)
    l = len(words[0])

    # initialize the count with the counter size
    count = len(c_r)

    while j < len(s):
        # Some init cal.
        if s[j:j+l] in c_r:
            c_r[s[j:j+l]] -= 1
            # if char count goes to 0 then we need to decrease the total variable count
            print(s[j:j+l], c_r[s[j:j+l]])
            if c_r[s[j:j+l]] == 0:
                count -= 1

        # make window of size len(words)
        if j+l-i < len(words)*l:
            j += l

        elif j+l-i == len(words)*l:
            # Do some other cal
            # When there's no element in the counter/map the count will go to 0
            if count == 0:
                g_r.append(i)

            #  as we move forward we need to inc the count of the element at postition i if it's decreased before.
            if s[i:i+l] in c_r:
                c_r[s[i:i+l]] += 1

            #  we inc the variable count only once and if there's a duplicate element the if condition will be ignored.
            if c_r[s[i:i+l]] == 1:
                count += 1
            # Remove the ith element from the window cal and then move the window
            i += l
            j += l

    return g_r


print(count_occurrences("lingmindraboofooowingdingbarrwingmonkeypoundcake", [
      "fooo", "barr", "wing", "ding", "wing"]))
