#! It's more like a fibonacci series only
def gridTravellerBasic(r, c, memo={}):
    if (r, c) in memo:
        return memo[(r, c)]
    if r == 1 and c == 1:
        return 1

    if r == 0 or c == 0:
        return 0

    memo[(r, c)] = gridTravellerBasic(r - 1, c, memo) + gridTravellerBasic(
        r, c - 1, memo
    )
    return memo[(r, c)]


print(gridTravellerBasic(1, 2))
print(gridTravellerBasic(2, 3))
print(gridTravellerBasic(3, 2))
print(gridTravellerBasic(3, 3))
