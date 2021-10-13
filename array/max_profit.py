import snoop


@snoop
def max_profit(arr):

    m_p, min_price = 0, arr[0]

    for i in arr:
        # This will keep track of min value
        min_price = min(i, min_price)
        # This will evaluate the profit based on the min price and current value as we iterate over the array
        profit = i - min_price
        # this will store the max profit in the m_p variable
        m_p = max(m_p, profit)

    return m_p


print(max_profit([7, 1, 2, 3, 11]))
