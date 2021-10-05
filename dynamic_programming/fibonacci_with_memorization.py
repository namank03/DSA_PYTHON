import snoop

# 1,1,2,3,5,8,13,21...


# Few Tips -
# 1. If we're getting None + int error then we probably want to check the return value. There must be a case where we're not returning  any value and therefore None is getting passed on the call stack above

# 1,1,2,3,5,8,13,21...
@snoop
def fibnumber(n, memo={}):
    # If the number is seen before and is available in the memo, then take the value from the memo and return
    if n in memo:
        return memo[n]
    # Base case as the 1st 2 numbers of the fibonacci series are 1
    if n <= 2:
        return 1
    # store the answer in the memo
    memo[n] = fibnumber(n - 1, memo) + fibnumber(n - 2, memo)
    # return the answer from the memo
    return memo[n]


fibnumber(5)
