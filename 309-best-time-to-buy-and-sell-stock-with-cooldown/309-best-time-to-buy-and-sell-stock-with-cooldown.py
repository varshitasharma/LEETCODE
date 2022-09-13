class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, bought, hold, l = 0, -prices[0], 0, len(prices)
        for price in prices:
            old_hold = hold
            hold = max(hold, sold)
            sold = price+ bought
            bought = max( old_hold - price, bought )
        return max(sold, hold)