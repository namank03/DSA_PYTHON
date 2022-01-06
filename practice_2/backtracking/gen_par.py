def gen_paren(o, c, op=""):

    if o == 0 and c == 0:
        print(f'op -> {op}')

    if o < 0 or c < 0 or c < o:
        return

    gen_paren(o - 1, c, op + '(') or gen_paren(o, c - 1, op + ')')


gen_paren(3, 3)
