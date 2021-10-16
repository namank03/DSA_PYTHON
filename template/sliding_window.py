import math
from typing import Counter


def sliding_window(s: str, t: str):

    # init a collection or int value to save the result according the question.
    result = []
    if(len(t) > len(s)):
        return result

    # create a hashmap to save the Characters of the target substring.
    # (K, V) = (Character, Frequency of the Characters)
    counter = Counter(t)

    # maintain a counter to check whether match the target string.
    # must be the map size, NOT the string size because the char may be duplicate.
    size = len(counter)

    # Two Pointers: begin - left pointer of the window; end - right pointer of the window
    begin = end = 0

    # the length of the substring which match the target string.
    length = math.inf

    # loop at the begining of the source string
    while end < len(s):

        c = s[end]

        if(c in counter):
            # plus or minus one
            counter[c] -= 1
            if(map.get(c) == 0):
                # modify the size according the requirement(different condition).
                size -= 1

        end += 1

        # increase begin pointer to make it invalid/valid again
        # size condition. different question may have different condition
        while size == 0:
            # ***be careful here: choose the char at begin pointer, NOT the end
            tempc = s[begin]
            if(tempc in map):
                # plus or minus one
                counter[tempc] += 1
                if(counter[tempc] > 0):
                    size += 1

            #  save / update(min/max) the result if find a target
            # result collections or result int value

            begin += 1
    return result
