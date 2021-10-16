def dna_seq(s):
    k = 10
    i = j = 0
    g_r = set()
    seq = set()
    c_r = ""

    while j < len(s):
        c_r += s[j]

        if j-i+1 < k:
            j += 1

        elif j-i+1 == k:
            if c_r in seq:
                g_r.add(c_r)
            seq.add(c_r)

            c_r = c_r[1:]
            i += 1
            j += 1

    return g_r


print(dna_seq("AAAAAAAAAAAAA"))
