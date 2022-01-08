def prod_arr_except_self(a):
    p = [1]
    for i in a[:-1]:
        p.append(p[-1] * i)

    k = [1]
    for i in a[::-1][:-1]:
        k.append(k[-1] * i)

    for index, (i, j) in enumerate(zip(p, k[::-1])):
        a[index] = i * j

    return a


a = [2, 4, 6, 8]
print(prod_arr_except_self(a))


# def prod_arr_except_self(a):
#     p = [1]
#     k = [1]
#     for i, j in zip(a[:-1], a[::-1][:-1]):
#         p.append(p[-1] * i)
#         k.append(k[-1] * j)

#     for index, (i, j) in enumerate(zip(p, k[::-1])):
#         a[index] = i * j

#     return a


# a = [2, 4, 6, 8]
# print(prod_arr_except_self(a))
