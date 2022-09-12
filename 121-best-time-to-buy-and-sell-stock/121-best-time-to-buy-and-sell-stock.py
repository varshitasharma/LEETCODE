class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp, minPrice = [0]*len(prices), prices[0]
        for i, price in enumerate(prices):
            minPrice = min( minPrice, price)
            if i>0: dp[i] = max(dp[i-1], price-minPrice)
        return dp[-1]