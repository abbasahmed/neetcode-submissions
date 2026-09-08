class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        lowest = prices[0]
        for i, p in enumerate(prices):
            if p < lowest:
                lowest = p
            maxprofit = max(maxprofit, p - lowest)
        return maxprofit
            
        