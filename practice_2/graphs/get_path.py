graph = {
    1: [2, 3],
    2: [4, 5],
    5: [6],
    4: [8],
    3: [7],
    7: [],
    6: [],
    8: [],
}

src = 1
dst = 4


def get_path(src, dst, path=[]):
    if src == dst:
        return path + [src]
    for neighbor in graph[src]:
        res = get_path(neighbor, dst, path + [src])
        if res:
            return res


res = get_path(src, dst)
print(f'res -> {res}')


def get_path2(src, dst):
    if src == dst:
        return [src]
    for neighbor in graph[src]:
        res = get_path2(neighbor, dst)
        if res:
            #! early return
            return res + [src]


res = get_path2(src, dst)
print(f'res -> {res}')
