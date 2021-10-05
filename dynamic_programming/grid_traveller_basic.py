def gridTravellerBasic(r, c):
    if r == 1 or c == 1:
        return 1

    if r == 0 or c == 0:
        return 0

    return gridTravellerBasic(r - 1, c) + gridTravellerBasic(r, c - 1)


print(gridTravellerBasic(1, 2))
print(gridTravellerBasic(2, 3))
print(gridTravellerBasic(3, 2))
print(gridTravellerBasic(3, 3))
