class Solution:
    def maxProfit(self, prices) -> int:

        # ! Trick is to keep track of the min price and max profit
        m_p, min_price = 0, prices[0]

        for i in prices:
            min_price = min(i, min_price)
            profit = i - min_price
            m_p = max(m_p, profit)

        return m_p
