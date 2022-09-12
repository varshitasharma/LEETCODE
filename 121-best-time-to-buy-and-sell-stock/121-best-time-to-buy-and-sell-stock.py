class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans, minPrice = 0, prices[0]
        for i in range(len(prices)): 
            ans = max(ans, prices[i]-minPrice)
            minPrice = min( minPrice, prices[i])
        return ans