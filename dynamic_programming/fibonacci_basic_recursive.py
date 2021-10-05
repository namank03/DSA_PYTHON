import snoop


@snoop
def fibnumber(n):
    # Base case as the 1st 2 numbers of the fibonacci series are 1
    if n <= 2:
        return 1
    return fibnumber(n - 1) + fibnumber(n - 2)


fibnumber(5)
