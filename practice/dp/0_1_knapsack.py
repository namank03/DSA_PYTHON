# weight = [1,2,3,10]
# price = [30,200,1,10000]
# capacity = 5


def solve(weight, price, capactiy):
    # if weight is empty or capacity is 0 then return 0
    if not weight or capactiy == 0:
        return 0

    # if weight is not empty and capacity is not 0 then
    # see if we can place the item in a bag or not?
    # if we can then we will take the item and recursively call the function
    # with the remaining weight and remaining capacity
    # if we cannot then we will not take the item and recursively call the function
    # with the remaining weight and remaining capacity
    if weight[0] <= capactiy:
        return max(
            price[0] + solve(weight[1:], price[1:], capactiy - weight[0]),
            solve(weight[1:], price[1:], capactiy),
        )
    else:
        return solve(weight[1:], price[1:], capactiy)


res = solve([1, 2, 3, 10], [30, 200, 1, 10000], 10)
print(f'res -> {res}')
